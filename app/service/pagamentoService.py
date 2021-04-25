import uuid
from app.model.response import Response, getResponse
import json
from cacheout import Cache
from fastapi.exceptions import HTTPException
from fastapi import logger
import requests
from settings import API_TOKEN_IUGU, URL_API_IUGU_CUSTOMERS, URL_API_PAGAMENTO, URL_CRIAR_SUB_CONTA,URL_ENVIA_CONTA_VERIFICACAO
from app.model.formadePagamentoiugu import FormaDePagamentoIugu
from app.model.formapgtoModel import FormaPagamentoModel
from app.data.pagamentosData import CadastraFormaPgtoUsuario, BuscarFormasPagamento, GravaTransacaoAutorizadaDb,GravaDadosSubContaProfissional, BuscarSubConta,GravaVerificacaoContaRetorno,GravaSolicitacaoSaque
from app.model.requestPagamentoModel import RequestPagamentoModel
from app.model.responsePagamentoModel import ResponsePagamentoModel
from app.model.subContaRequestModel import SubContaRequestModel
from app.model.subContaResponseModel import SubContaResponseModel
from app.data.usuarioData import BuscarProfissionalData, BuscarEmpresaData
from app.model.verificacaoContaModel import VerificacaoContaModel
from app.model.pedidosaqueModel import PedidoSaqueModel
from datetime import datetime  

def CriarFormaPagamentoService(formapgto: FormaDePagamentoIugu):
    url = URL_API_IUGU_CUSTOMERS + "/" + formapgto.idClienteIugu + "/payment_methods"

    # token gerado no painel
    querystring = {"api_token": API_TOKEN_IUGU}

    payload = {
        "token": formapgto.tokenGeradoIugu,  #token do cartao gerado no html
        "description": formapgto.Descricao,
        "set_as_default": formapgto.CartaoPrincipal
    }

    headers = {"Content-Type": "application/json"}
    response = requests.request(
        "POST", url, json=payload, headers=headers, params=querystring)

    metodoPagamentoUsuario = FormaPagamentoModel(response.json()['id'], response.json()['description'], response.json()['item_type'],
                                                 response.json()['customer_id'], response.json()['data'])

    CadastraFormaPgtoUsuario(metodoPagamentoUsuario)
    return response.json()

def BuscarFormasPagamentoService(IdUsuarioIugu: str):
    return BuscarFormasPagamento(IdUsuarioIugu)

def EfetuarPagamentoService(pgto: RequestPagamentoModel):

    # test_api_token da subconta
    querystring = {"api_token": pgto.tokenSubConta}
    payload = {
        "items": [
            {
                "description": pgto.DescricaoProduto,
                "quantity": 1,
                "price_cents": pgto.Valor.replace(',', '').replace('.', '')
            }
        ],
        "customer_payment_method_id": pgto.IdFormaPagtoIugu,  # id da forma de pagamento
        # id do cliente na base da iugu, cliente q vai pagar
        "customer_id": pgto.IdUsuarioIugu,
        "email": pgto.EmailUsuario,
        "bank_slip_extra_days": 3,
        "keep_dunning": True
    }

    headers = {"Content-Type": "application/json"}
    response = requests.request(
        "POST", URL_API_PAGAMENTO, json=payload, headers=headers, params=querystring)

    try:
        if  len(response.json()['errors']) == 0:
            result = ResponsePagamentoModel(response.json()['status'],response.json()['info_message'],response.json()['reversible'], response.json()['token'],
                                            response.json()['brand'], response.json()['bin'], response.json()['success'],
                                            response.json()['url'], response.json()['pdf'],response.json()['identification'], response.json()['invoice_id'], 
                                            response.json()['LR'])

            GravaTransacaoAutorizadaDb(result,pgto.IdUsuarioIugu)

            return result
        else:
            return response.json()

    except Exception as mensagemErro:
        return mensagemErro

def CriarSubContaService(info: SubContaRequestModel):
    
    querystring = {"api_token":info.ApiTokenIugu} #token de produção

    payload = {
        "commissions": {
            "percent": info.ComissaoPorcentagem,
            "cents": info.ValorEmRealComissao.replace(',', '').replace('.', ''),
            "credit_card_percent": info.ComissaoPorcentagem,
            "bank_slip_cents": info.ComissaoPorcentagem,
            "bank_slip_percent": info.ComissaoPorcentagem,
            "pix_cents": info.ComissaoPorcentagem,
            "pix_percent": info.ComissaoPorcentagem,
            "permit_aggregated": True,
            "credit_card_cents": info.ComissaoPorcentagem
        },
        "name": info.NomeSubConta
    }

    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", URL_CRIAR_SUB_CONTA, json=payload, headers=headers, params=querystring)

    _subconta = SubContaResponseModel(response.json()['account_id'],response.json()['name'],response.json()['live_api_token'],response.json()['test_api_token'],
    response.json()['user_token'],response.json()['commissions'])

    GravaDadosSubContaProfissional(_subconta,info.IdUsuarioIugu)

    return response.json()

def BuscarSubContaService(IdUsuarioIugu:str):
    return BuscarSubConta(IdUsuarioIugu)

def EnviaVerificacaoSubConta(IdUsuario:int,IdSubConta:str,TokenSubContaPrd:str, IdPerfil: int):
    headers = {"Content-Type": "application/json"}

    url = URL_ENVIA_CONTA_VERIFICACAO + IdSubConta + "/request_verification" #ID da sub-conta

    querystring = {"api_token":TokenSubContaPrd} #Token de Produção que vem no response da criação da subconta;

    if IdPerfil == 2:
        user = BuscarProfissionalData(IdUsuario)
        payload = {"data": {
                "price_range": "Entre R$ 100,00 e R$ 500,00",
                "physical_products": False,
                "business_type": "Telemed - Atendimento Médico",
                "person_type": "Pessoa Física",
                "automatic_transfer": True,
                "cpf": user.Cpf,
                "name": user.Nome,
                "address": user.Endereco,
                "cep": user.Cep,
                "city": user.Cidade,
                "state": user.Estado,
                "telephone": user.Telefone,
                "bank": user.ContasCorrente[0].Banco,
                "bank_ag": user.ContasCorrente[0].Agencia,
                "account_type": "Corrente",
                "bank_cc": str(user.ContasCorrente[0].ContaCorrente) + "-" + str(user.ContasCorrente[0].DigitoVerificador)
            }}


    if IdPerfil == 3:
        user = BuscarEmpresaData(IdUsuario)
        bancocc= str(user.ContasCorrente[0].ContaCorrente) + "-" + str(user.ContasCorrente[0].DigitoVerificador)
        vank= user.ContasCorrente[0].Banco

        payload = {"data": {
        "price_range": "Entre R$ 100,00 e R$ 500,00",
        "physical_products": False,
        "business_type": "Telemed - Atendimento Médico",
        "person_type": "Pessoa Jurídica",
        "automatic_transfer": True,
        "address": user.Endereco,
        "cep": user.Cep,
        "city": user.Cidade,
        "state": user.Estado,
        "telephone": user.TelefoneCorporativoEmp,
        "bank": user.ContasCorrente[0].Banco,
        "bank_ag": user.ContasCorrente[0].Agencia,
        "account_type": "Corrente",
        "bank_cc": str(user.ContasCorrente[0].ContaCorrente) + "-" + str(user.ContasCorrente[0].DigitoVerificador),
        "cnpj": user.Cnpj,
        "company_name": user.NomeEmpresaEmp,
        "resp_name": user.Nome
    }}
    
    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

    if  'errors' in response.json():
            return response.json()

    result = VerificacaoContaModel(IdSubConta,IdPerfil,TokenSubContaPrd, response.text,IdUsuario, user.idUsuarioIugu)

    #cadastra response verificacao conta:
    GravaVerificacaoContaRetorno(result)

    return response.json()


def SolicitaSaqueSubConta(TokenSubContaPrd:str,IdSubConta:str, ValorSaque:str, IdUsuario:int):
    
    url = URL_ENVIA_CONTA_VERIFICACAO + IdSubConta + "/request_withdraw" #idSubConta
    querystring = {"api_token":TokenSubContaPrd} #Token da subconta de produção
    payload = {"amount": ValorSaque.replace(',', '').replace('.', '')}
    headers = {"Content-Type": "application/json"}
    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

    if response.status_code == 200:
        result = PedidoSaqueModel(0,IdSubConta, ValorSaque.replace('.', '').replace(',', ''), 
                                    IdUsuario, datetime.now(), response.json()['id'])
        GravaSolicitacaoSaque(result)
        return response.json()

    return response.json()