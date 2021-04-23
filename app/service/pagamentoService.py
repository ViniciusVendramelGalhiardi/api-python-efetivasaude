import uuid
from app.model.response import Response, getResponse
import json
from cacheout import Cache
from fastapi.exceptions import HTTPException
from fastapi import logger
import requests
from settings import API_TOKEN_IUGU, URL_API_IUGU_CUSTOMERS
from app.model.formadePagamentoiugu import FormaDePagamentoIugu
from app.model.formapgtoModel import FormaPagamentoModel
from app.data.pagamentosData import CadastraFormaPgtoUsuario, BuscarFormasPagamento

def CriarFormaPagamentoService(formapgto: FormaDePagamentoIugu):
    url = URL_API_IUGU_CUSTOMERS + "/" + formapgto.idClienteIugu + "/payment_methods"
    
    # token gerado no painel
    querystring = {"api_token": API_TOKEN_IUGU}
    
    payload = {
        "token": formapgto.tokenGeradoIugu, #token do cartao gerado no html
        "description": formapgto.Descricao,
        "set_as_default": formapgto.CartaoPrincipal
    }

    headers = {"Content-Type": "application/json"}
    response = requests.request(
        "POST", url, json=payload, headers=headers, params=querystring)

    metodoPagamentoUsuario = FormaPagamentoModel(response.json()['id'],response.json()['description'], response.json()['item_type'],
                            response.json()['customer_id'],response.json()['data'])
    
    CadastraFormaPgtoUsuario(metodoPagamentoUsuario)

    return response.json()

def BuscarFormasPagamentoService(IdUsuarioIugu: str):
    return BuscarFormasPagamento(IdUsuarioIugu)