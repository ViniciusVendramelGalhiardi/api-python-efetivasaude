from app.data.usuarioData import CadastrarCartao
from fastapi import APIRouter, FastAPI, HTTPException, Request, Response, logger
from typing import Optional
from pydantic import BaseModel
import json
from app.model.response import getResponse
from app.service.ListagemService import listaPerfil, listaAbordagem, listaHobbies, listaCRP, listaHorarioTrabalho, listaIdiomas, listaNosConheceu, listaPlanos, listaProfissao, listaSintomas, listaUsarPlataforma
from app.model.usuarioModel import UsuarioModel
from fastapi.responses import JSONResponse
from app.service.usuarioService import EfetuaLoginUsuarioService, EditarUsuario, CadastrarUsuario, BuscaUsuarioService, CadastraExpedienteProfissional, ListarExpedienteProfissional, VincularSintomaProfissionalService, BuscarSintomaPorUsuarioDataService, CadastrarCartaoService, BuscarCartaoUsuarioService, ExcluirCartaoService, EnviarSmsUsuarioService, BuscarProfissionalPorPesquisa, CadastraExperienciaService, AtualizaExperienciaService, ExcluirExperienciaService, CadastraFormacaoService, AtualizaFormacaoService, ExcluirFormacaoService, CadastraDependenteService, AtualizaDependenteService, ExcluirDependenteService, ListarHistoricoAtendimentoService, CadastrarProntuarioService, ListaProntuarioPacienteService, AtualizaProntuarioService, AtualizaSenhaUsuarioService, CadastrarColaboradoreEmpresaService, ListaColaboradoresEmpresaService,BuscarDezUltimosCadastradosService
from app.model.expedienteProfissionalModel import ExpedienteProfissionalModel
from app.service.agendaService import efetuaAgendamentoService, listarAgendamentosProfissional, atualizaStatusService, cadastraAvaliacaoService, buscarAvaliacaoProfissionalService
from app.model.agendamentoConsultaModel import AgendamentoConsultaModel
from app.model.avaliacaoefModel import AvaliacaoEfModel
from app.model.sintomasVinculadosModel import SintomasVinculadosModel
from typing import List
from app.model.cartaoModel import CartaoModel
from app.model.experienciaPraticaModel import ExperienciaPraticaModel
from app.model.formacaoAcademiaModel import FormacaoAcademicaModel
from app.model.dependenteModel import DependenteModel
from app.model.usuarioPronturioModel import UsuarioProntuarioModel
from app.model.colaboradoresEmpresa import ColaboradoresEmpresa
from typing import  Optional

router_web = APIRouter(
    prefix="/web",
    tags=["web"]
)


@router_web.post("/cadastrarUsuario/{IdPerfil}")
async def cadastrar(IdPerfil: int, UsuarioModel: UsuarioModel):
    response = CadastrarUsuario(IdPerfil, UsuarioModel)
    tt = response
    return response


@router_web.post("/editarUsuario/{IdPerfil}")
async def edit(IdPerfil: int, UsuarioModel: UsuarioModel):
    response = EditarUsuario(IdPerfil, UsuarioModel, UsuarioModel.IdUsuario)
    tt = response
    return response


@router_web.post("/EfetuaLogin/")
async def EfetuaLoginUsuario(email: str, senha: str, idperfil: int):
    response = EfetuaLoginUsuarioService(email, senha, idperfil)
    return response


@router_web.post("/CadastrarProntuarioMedico/")
async def CadastrarProntuario(pront: UsuarioProntuarioModel):
    response = CadastrarProntuarioService(pront)
    return response


@router_web.post("/cadastraExpediente/")
async def CadastraEspedienteProfissional(expediente: ExpedienteProfissionalModel):
    response = CadastraExpedienteProfissional(expediente)
    return response


@router_web.post("/CadastrarColaborador/")
async def CadastrarColaboradorEmp(col: ColaboradoresEmpresa):
    response = CadastrarColaboradoreEmpresaService(col)
    return response


@router_web.post("/efetuaAgendamento/")
async def EfetuaAgendamento(ag: AgendamentoConsultaModel):
    response = efetuaAgendamentoService(ag)
    return response


@router_web.post("/atualizarStatusAgendamento/")
async def atualizarStatusAgendamento(IdAgenda: int, StatusAgendamento: str):
    response = atualizaStatusService(IdAgenda, StatusAgendamento)
    return response


@router_web.post("/AtualizaProntuarioMedico/")
async def AtualizaProntuario(pront: UsuarioProntuarioModel):
    response = AtualizaProntuarioService(pront)
    return response


@router_web.post("/cadastraAvaliacaoService/")
async def CadastraAvaliacaoService(av: AvaliacaoEfModel):
    response = cadastraAvaliacaoService(av)
    return response


@router_web.post("/cadastraSintomas/")
async def VinculaSintomasAtendidosProf(sin: List[SintomasVinculadosModel]):
    response = VincularSintomaProfissionalService(sin)
    return response


@router_web.post("/cadastraDependente/")
async def CadastraDepend(dep: DependenteModel):
    response = CadastraDependenteService(dep)
    return response


@router_web.put("/atualizaDependente/{IdDependente}")
async def AtualizaDepend(IdDependente: int, dep: DependenteModel):
    response = AtualizaDependenteService(IdDependente, dep)
    return response


@router_web.delete("/excluirDependente/{IdDependente}")
async def ExcluirDepend(IdDependente: int):
    response = ExcluirDependenteService(IdDependente)
    return response


@router_web.post("/cadastraExperienciaProf/")
async def CadastraExperiencia(exp: ExperienciaPraticaModel):
    response = CadastraExperienciaService(exp)
    return response


@router_web.put("/atualizaExperienciaProf/{IdExperiencia}")
async def AtualizaExperiencia(IdExperiencia: int, exp: ExperienciaPraticaModel):
    response = AtualizaExperienciaService(IdExperiencia, exp)
    return response


@router_web.put("/AtualizaSenhaUsuario/{email}")
async def AtualizaSenhaUsuarioCadastrado(email: str, senhaatual: str, novasenha: str, IdUsuario: int):
    response = AtualizaSenhaUsuarioService(
        email, senhaatual, novasenha, IdUsuario)
    return response


@router_web.delete("/excluirExperienciaProf/{IdExperiencia}")
async def ExcluirExperiencia(IdExperiencia: int):
    response = ExcluirExperienciaService(IdExperiencia)
    return response


@router_web.post("/cadastraFormacaoProf/")
async def CadastraFormacao(formacao: FormacaoAcademicaModel):
    response = CadastraFormacaoService(formacao)
    return response


@router_web.put("/atualizaFormacaoProf/{IdFormacao}")
async def AtualizaFormacao(IdFormacao: int, formacao: FormacaoAcademicaModel):
    response = AtualizaFormacaoService(IdFormacao, formacao)
    return response


@router_web.delete("/excluirFormacaoProf/{IdFormacao}")
async def ExcluirFormacao(IdFormacao: int):
    response = ExcluirFormacaoService(IdFormacao)
    return response


@router_web.delete("/ExcluirCartaoUsuario/{idUsuario}")
async def ExcluirCartaoUsuario(idUsuario: int):
    response = ExcluirCartaoService(idUsuario)
    return response


@router_web.post("/CadastrarCartao/")
async def CadastrarCartaoUsuario(card: CartaoModel):
    response = CadastrarCartaoService(card)
    return response


@router_web.post("/EnviarSMS/{DDNumeroCelular}/{NomeCliente}")
async def EnviarSMSUsuario(DDNumeroCelular: str, NomeCliente: str):
    response = EnviarSmsUsuarioService(DDNumeroCelular, NomeCliente)
    return response


@router_web.get("/ListarHistorico/{IdProfissional}")
def ListarHistoricoAtendimento(IdProfissional: int):
    return ListarHistoricoAtendimentoService(IdProfissional)


@router_web.get("/ListaColaboradoresEmpresa/{IdProfissional}")
def ListaColaboradoresEmpresa(IdProfissional: int):
    return ListaColaboradoresEmpresaService(IdProfissional)


@router_web.get("/BuscarCartaoUsuario/{IdUsuario}")
def BuscarCartaoUsuario(IdUsuario: int):
    return BuscarCartaoUsuarioService(IdUsuario)

@router_web.get("/BuscarDezUltimosCadastrados/")
def BuscarDezUltimosCadastrados():
    return BuscarDezUltimosCadastradosService()



@router_web.get("/ListaProntuario/{IdUsuario}")
def ListaProntuarioPaciente(IdUsuario: int):
    return ListaProntuarioPacienteService(IdUsuario)


@router_web.get("/BuscarSintomaPorUsuario/{IdUsuario}")
def BuscarSintomaPorUsuario(IdUsuario: int):
    return BuscarSintomaPorUsuarioDataService(IdUsuario)


@router_web.get("/BuscarAvaliacaoProfissionalService/{IdUsuario}")
def BuscarAvaliacaoProfissionalService(IdUsuario: int):
    return buscarAvaliacaoProfissionalService(IdUsuario)


@router_web.get("/ListarAgendamentosProfissional/{IdUsuario}/{IdPerfil}")
def listarAgendamentoProf(IdUsuario: int, IdPerfil: int):
    return listarAgendamentosProfissional(IdUsuario, IdPerfil)


@router_web.get("/ListarExpedienteProfissional/{IdProfissional}")
def ListarExpProfissional(IdProfissional: int,  Status: Optional[str] = None, DataAtendimento: Optional[str] = None, IdExpediente: Optional[str] = None):
    return ListarExpedienteProfissional(IdProfissional, Status, DataAtendimento, IdExpediente)


@router_web.get("/ListarPerfis/")
def ListarPerfil():
    return listaPerfil()


@router_web.get("/BuscarUsuario/{idUsuario}/{idPerfil}")
def BuscarUsuario(idUsuario: str, idPerfil: int):

    try:
        response = BuscaUsuarioService(idUsuario, idPerfil)
    except Exception as mensagemErro:
        return mensagemErro
    return response


@router_web.get("/BuscarProfissionalPorPesq/{IdProfissao}/{AtendePresencialmenteProf}/{DataAtendimento}/{IdSintomaAtendido}/{IdAbordagemAdotada}/{Nome}")
def BuscarProfissional(IdProfissao: Optional[str], AtendePresencialmenteProf: Optional[str], DataAtendimento: Optional[str], IdSintomaAtendido: Optional[str], IdAbordagemAdotada: Optional[str], Nome: Optional[str]):
    try:
        response = BuscarProfissionalPorPesquisa(IdProfissao, AtendePresencialmenteProf, DataAtendimento, IdSintomaAtendido, IdAbordagemAdotada, Nome)
    except Exception as mensagemErro:
        return mensagemErro
    return response


@router_web.get("/ListarAbordagem/")
def ListaAbordagem():
    return listaAbordagem()


@router_web.get("/ListaHobbies/")
def ListaHobbies():
    return listaHobbies()


@router_web.get("/ListaCRP/")
def ListaCRP():
    return listaCRP()


@router_web.get("/ListaHorarioTrabalho/")
def ListaHorarioTrabalho():
    return listaHorarioTrabalho()


@router_web.get("/ListaIdiomas/")
def ListaIdiomas():
    return listaIdiomas()


@router_web.get("/ListaNosConheceu/")
def ListaNosConheceu():
    return listaNosConheceu()


@router_web.get("/ListaPlanos/")
def ListaPlanos():
    return listaPlanos()


@router_web.get("/ListaProfissao/")
def ListaProfissao():
    return listaProfissao()


@router_web.get("/ListaSintomas/")
def ListaSintomas():
    return listaSintomas()


@router_web.get("/ListaUsarPlataforma/")
def ListaUsarPlataforma():
    return listaUsarPlataforma()
