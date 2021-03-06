from app.model.usuarioModel import UsuarioModel
from app.entity.usuarioEntity import UsuarioEntity
from app.entity.profissionalEntity import ProfissionalEntity
from app.entity.dependetesEntity import DependentesEntity
from app.entity.empresaEntity import EmpresaEntity
from app.entity.experienciaspraticas import ExperienciasEntity
from app.entity.contasCorrente import ContasCorrenteEntity
from app.entity.atendimentoPresencialEntity import AtendimentoPresencialEntity
from app.entity.idiomasAtendidosEntity import IdiomasAtendidosEntity
from app.entity.formacaoAcademicaEntity import FormacaoAcademicaEntity
from app.entity.planoSaudeEmpresaUsuarioEntity import PlanodeSaudeEmpresaUsuarioEntity
from app.model.expedienteProfissionalModel import ExpedienteProfissionalModel, ExpedienteItem, Hora
from typing import List
from app.model.abordagemProfissionalModel import AbordagemProfissionalModel
from app.model.publicoAtendidoProfissionalModel import PublicoAtendidoProfissionalModel
from app.model.sintomasVinculadosModel import SintomasVinculadosModel
from app.model.cartaoModel import CartaoModel


class UsuarioFactory():

    def ExpedientesModel(expedientes):
        try:
            listexp = []

            for row in expedientes:
                dep = ExpedienteProfissionalModel(IdUsuarioProfissional=row[1])
                exp = ExpedienteItem()
                exp.Idexpediente = row[0]
                exp.Data = row[2]
                hr = Hora()
                hr.start = row[3]
                hr.end = row[4]
                hr.status = row[5]
                hr.online = row[6]
                dep.Expediente = exp
                dep.Expediente.Horas = hr
                listexp.append(dep)

        except Exception as e:
            print(e)
            return e

        return listexp

    def UsuarioModelToEntity(uModel: UsuarioModel):
        user = UsuarioEntity(
            Nome=uModel.Nome,
            Telefone=uModel.Telefone,
            Email=uModel.Email,
            Cidade=uModel.Cidade,
            Estado=uModel.Estado,
            Cep=uModel.Cep,
            Endereco=uModel.Endereco,
            IdConheceu=uModel.IdConheceu,
            Senha=uModel.Senha,
            TermosCondicoes=uModel.TermosCondicoes,
            PoliticaPrivacidade=uModel.PoliticaPrivacidade,
            Apelido=uModel.Apelido,
            EstadoCivil=uModel.EstadoCivil,
            PossuiFilhosQtd=uModel.PossuiFilhosQtd,
            IdHobbie=uModel.IdHobbie,
            DataNascimento=uModel.DataNascimento,
            Genero=uModel.Genero,
            IdProfissao=uModel.IdProfissao,
            Cpf=uModel.Cpf,
            Dependente=uModel.Dependente,
            Dependentes=uModel.Dependentes,
            BaseImage=uModel.BaseImage
        )

        return user

    def UsuarioEntityToModel(records, _dependentes):
        user = UsuarioEntity(
            Nome=records[0][0],
            Telefone=records[0][1],
            Email=records[0][2],
            Cidade=records[0][3],
            Estado=records[0][4],
            IdConheceu=records[0][5],
            TermosCondicoes=records[0][6],
            PoliticaPrivacidade=records[0][7],
            Apelido=records[0][8],
            EstadoCivil=records[0][9],
            PossuiFilhosQtd=records[0][10],
            IdHobbie=records[0][11],
            DataNascimento=records[0][12],
            Genero=records[0][13],
            IdProfissao=records[0][14],
            Cpf=records[0][15],
            idUsuario=records[0][16],
            Dependente=records[0][17],
            Dependentes=_dependentes,
            Cep=records[0][18],
            Endereco=records[0][19],
            IdUsuarioIugu=records[0][20],
            IdPerfil=records[0][21],
            BaseImage=records[0][22]
        )

        return user

    # NomeEmpresaEmp, TelefoneCorporativoEmp, EmailCorporativoEmp,SiteEmpr,LinkedinEmpr, InstagramEmp,CargoFuncaoEmp,NumeroColaboradoresEmp,Cnpj
    def EmpresaEntityToModel(records, _planos, _contacorrente):

        empr = EmpresaEntity(
            Nome=records[0][0],
            Telefone=records[0][1],
            Email=records[0][2],
            Cidade=records[0][3],
            Estado=records[0][4],
            IdConheceu=records[0][5],
            TermosCondicoes=records[0][6],
            PoliticaPrivacidade=records[0][7],
            Apelido=records[0][8],
            NomeEmpresaEmp=records[0][9],
            TelefoneCorporativoEmp=records[0][10],
            EmailCorporativoEmp=records[0][11],
            SiteEmpr=records[0][12],
            LinkedinEmpr=records[0][13],
            InstagramEmp=records[0][14],
            CargoFuncaoEmp=records[0][15],
            NumeroColaboradoresEmp=records[0][16],
            Cnpj=records[0][17],
            idUsuario=records[0][18],
            idUsuarioIugu=records[0][19],
            Cep=records[0][20],
            Endereco=records[0][21],
            PlanodeSaudeEmpresa=_planos,
            ContasCorrente=_contacorrente
        )

        return empr

    def ContaCorrenteEntityToModel(conta):
        listcc = []
        cc = ContasCorrenteEntity(
            IdContaBancaria=conta[0][0],
            Banco=conta[0][1],
            Agencia=conta[0][2],
            ContaCorrente=conta[0][3],
            DigitoVerificador=conta[0][4],
            IdUsuario=conta[0][5]
        )
        listcc.append(cc)
        return listcc

    def AtendimentoEntityToModel(atendimento):
        listatp = []
        atp = AtendimentoPresencialEntity(
            IdAtendimentoPresencial=atendimento[0][0],
            Endereco=atendimento[0][1],
            Numero=atendimento[0][2],
            Conjunto=atendimento[0][3],
            Bairro=atendimento[0][4],
            Cidade=atendimento[0][5],
            Estado=atendimento[0][6],
            Cep=atendimento[0][7],
            IdUsuario=atendimento[0][8]
        )
        listatp.append(atp)
        return listatp

    def DependenteEntityToModel(dependentes):
        listdep = []

        for row in dependentes:
            dep = DependentesEntity(
                IdDependente=row[0],
                Nome=row[1],
                Apelido=row[2],
                DataNascimento=row[3],
                Genero=row[4],
                Telefone=row[5],
                Email=row[6],
                Cpf=row[7],
                IdUsuario=row[8]
            )
            listdep.append(dep)
        return listdep

    def PlanosEntityToModel(planos):
        listplanos = []

        for row in planos:

            plan = PlanodeSaudeEmpresaUsuarioEntity(
                Id=row[0],
                IdPlanoCredenciado=row[1],
                IdUsuario=row[2]
            )

            listplanos.append(plan)

        return listplanos

    def IdiomasEntityToModel(idiomas):
        listidiomas = []

        for row in idiomas:
            idi = IdiomasAtendidosEntity(
                Ididioma=row[0],
                idUsuario=row[1]
            )
            listidiomas.append(idi)

        return listidiomas

    def FormacoesEntityToModel(formacoes):
        listformacoes = []

        for row in formacoes:
            formacao = FormacaoAcademicaEntity(
                IdFormacao=row[0],
                IdUsuario=row[1],
                InstituicaoEnsino=row[2],
                NomeCurso=row[3],
                NivelAcademico=row[4],
                AnoInicio=row[5],
                AnoTermino=row[6],
                DescricaoCurso=row[7],
                Anexo=row[8]
            )
            listformacoes.append(formacao)
        return listformacoes

    def AbordagemEntityToModel(abordagens):
        listabordagens = []

        for row in abordagens:
            abordagem = AbordagemProfissionalModel(
                IdAbordagemAdotada=row[0]
            )
            listabordagens.append(abordagem)

        return listabordagens

    def PublicoAlvoEntityToModel(publicoalvo):
        listapublicoalvo = []

        for row in publicoalvo:
            palvo = PublicoAtendidoProfissionalModel(
                IdPublicoAtendido=row[0]
            )
            listapublicoalvo.append(palvo)

        return listapublicoalvo

    def ExperienciasEntityToModel(experiencias):
        listdep = []

        for row in experiencias:
            dep = ExperienciasEntity(
                IdExperiencia=row[0],
                IdUsuario=row[1],
                TipoExperiencia=row[2],
                AtividadePrincipal=row[3],
                Descricao=row[4],
                DataInicio=row[5],
                DataTermino=row[6]
            )

            listdep.append(dep)

        return listdep

    def ProfissionalModelToEntity(uModel: UsuarioModel):

        try:
            prof = ProfissionalEntity(
                Nome=uModel.Nome,
                Telefone=uModel.Telefone,
                Email=uModel.Email,
                Cidade=uModel.Cidade,
                Estado=uModel.Estado,
                Cep=uModel.Cep,
                Endereco=uModel.Endereco,
                IdConheceu=uModel.IdConheceu,
                Senha=uModel.Senha,
                TermosCondicoes=uModel.TermosCondicoes,
                PoliticaPrivacidade=uModel.PoliticaPrivacidade,
                Apelido=uModel.Apelido,
                EstadoCivil=uModel.EstadoCivil,
                PossuiFilhosQtd=uModel.PossuiFilhosQtd,
                IdHobbie=uModel.IdHobbie,
                DataNascimento=uModel.DataNascimento,
                Genero=uModel.Genero,
                IdProfissao=uModel.IdProfissao,
                Cpf=uModel.Cpf,
                Dependente=uModel.Dependente,
                Dependentes=uModel.Dependentes,
                IdHorarioTrabalhoProf=uModel.IdHorarioTrabalhoProf,
                IdUsarPlataformaProf=uModel.IdUsarPlataformaProf,
                IdConselhoRegionalProf=uModel.IdConselhoRegionalProf,
                PossuiCNPJProf=uModel.PossuiCNPJProf,
                TrabalharComCNPJProf=uModel.TrabalharComCNPJProf,
                Cnpj=uModel.Cnpj,
                CartaApresentacaoProf=uModel.CartaApresentacaoProf,

                OutraAbordagemProf=uModel.OutraAbordagemProf,
                IdAbordagemProf=uModel.IdAbordagemProf,

                DuracaoAtendimentoProf=uModel.DuracaoAtendimentoProf,
                AtendePlanoDeSaudeProf=uModel.AtendePlanoDeSaudeProf,
                ReciboReembolsavelProf=uModel.ReciboReembolsavelProf,
                AtendePresencialmenteProf=uModel.AtendePresencialmenteProf,
                PrimeiroClienteCobraProf=uModel.PrimeiroClienteCobraProf,
                PrimeiroClienteValorFixoProf=uModel.PrimeiroClienteValorFixoProf,
                EmpresasParceirasDescontoProf=uModel.EmpresasParceirasDescontoProf,
                ValorPorSessaoProf=uModel.ValorPorSessaoProf,
                ExperienciasPraticaProf=uModel.ExperienciasPraticaProf,
                FormacoesProf=uModel.FormacoesProf,
                IdiomasAtendidosProf=uModel.IdiomasAtendidosProf,
                AtendimentoPresencialProf=uModel.AtendimentoPresencialProf,
                ContasCorrente=uModel.ContasCorrente,
                RegistroCRPePsi=uModel.RegistroCRPePsi,
                RegistroePsiValidado=uModel.RegistroePsiValidado,
                IdsPublicoAtendido=uModel.IdsPublicoAtendido,
                OutroPublicoProf=uModel.OutroPublicoProf,
                OutroIdiomaProf=uModel.OutroIdiomaProf,
                BaseImage=uModel.BaseImage
            )

        except Exception as e:
            return e

        return prof

    # records, listCC, listAtp, listIdiomas, listFormacoes, listexperiencias)

    def ProfEntityToModel(records, _contacorrente,
                          _atendimentospresenciais, _idiomasAtendidos, _formacoesProf, _experienciasPraticaProf, _listabordagem, _idspublicoAtendido):

        try:
            prof = ProfissionalEntity(
                Nome=records[0][0],
                Telefone=records[0][1],
                Email=records[0][2],
                Cidade=records[0][3],
                Estado=records[0][4],
                IdConheceu=records[0][5],
                TermosCondicoes=records[0][6],
                PoliticaPrivacidade=records[0][7],
                Apelido=records[0][8],
                EstadoCivil=records[0][9],
                PossuiFilhosQtd=records[0][10],
                IdHobbie=records[0][11],
                DataNascimento=records[0][12],
                Genero=records[0][13],
                IdProfissao=records[0][14],
                Cpf=records[0][15],
                IdHorarioTrabalhoProf=records[0][16],
                IdUsarPlataformaProf=records[0][17],
                IdConselhoRegionalProf=records[0][18],
                PossuiCNPJProf=records[0][19],
                TrabalharComCNPJProf=records[0][20],
                Cnpj=records[0][21],
                CartaApresentacaoProf=records[0][22],
                OutraAbordagemProf=records[0][23],
                DuracaoAtendimentoProf=records[0][24],
                AtendePlanoDeSaudeProf=records[0][25],
                ReciboReembolsavelProf=records[0][26],
                AtendePresencialmenteProf=records[0][27],
                PrimeiroClienteCobraProf=records[0][28],
                PrimeiroClienteValorFixoProf=records[0][29],
                EmpresasParceirasDescontoProf=records[0][30],
                ValorPorSessaoProf=records[0][31],
                idUsuario=records[0][32],
                Cep=records[0][33],
                Endereco=records[0][34],
                idUsuarioIugu=records[0][35],
                IdPerfil=records[0][36],
                RegistroCRPePsi=records[0][37],
                RegistroePsiValidado=records[0][38],
                OutroPublicoProf=records[0][39],
                OutroIdiomaProf=records[0][40],
                BaseImage=records[0][41],
                ExperienciasPraticaProf=_experienciasPraticaProf,
                FormacoesProf=_formacoesProf,
                IdiomasAtendidosProf=_idiomasAtendidos,
                AtendimentoPresencialProf=_atendimentospresenciais,
                ContasCorrente=_contacorrente,
                IdAbordagemProf=_listabordagem,
                IdsPublicoAtendido=_idspublicoAtendido
            )

        except Exception as mensagemErro:
            return mensagemErro

        return prof

    def profissionalEntity(records):
        lst = []
        for row in records:
            try:
                prof = ProfissionalEntity(
                    Nome=row[0],
                    Telefone=row[1],
                    Email=row[2],
                    Cidade=row[3],
                    Estado=row[4],
                    IdConheceu=row[5],
                    TermosCondicoes=row[6],
                    PoliticaPrivacidade=row[7],
                    Apelido=row[8],
                    EstadoCivil=row[9],
                    PossuiFilhosQtd=row[10],
                    IdHobbie=row[11],
                    DataNascimento=row[12],
                    Genero=row[13],
                    IdProfissao=row[14],
                    Cpf=row[15],
                    IdHorarioTrabalhoProf=row[16],
                    IdUsarPlataformaProf=row[17],
                    IdConselhoRegionalProf=row[18],
                    PossuiCNPJProf=row[19],
                    TrabalharComCNPJProf=row[20],
                    Cnpj=row[21],
                    CartaApresentacaoProf=row[22],
                    OutraAbordagemProf=row[23],
                    DuracaoAtendimentoProf=row[24],
                    AtendePlanoDeSaudeProf=row[25],
                    ReciboReembolsavelProf=row[26],
                    AtendePresencialmenteProf=row[27],
                    PrimeiroClienteCobraProf=row[28],
                    PrimeiroClienteValorFixoProf=row[29],
                    EmpresasParceirasDescontoProf=row[30],
                    ValorPorSessaoProf=row[31],
                    idUsuario=row[32],
                    Cep=row[33],
                    Endereco=row[34],
                    idUsuarioIugu=row[35],
                    IdPerfil=row[36],
                    RegistroCRPePsi=row[37],
                    RegistroePsiValidado=row[38],
                    OutroPublicoProf=row[39],
                    OutroIdiomaProf=row[40],
                    BaseImage=row[41]
                )
                lst.append(prof)
            except Exception as mensagemErro:
                return mensagemErro

        return lst

    def EmpresaModelToEntity(uModel: UsuarioModel):

        try:
            empr = EmpresaEntity(
                Nome=uModel.Nome,
                Telefone=uModel.Telefone,
                Email=uModel.Email,
                Cidade=uModel.Cidade,
                Estado=uModel.Estado,
                Cep=uModel.Cep,
                Endereco=uModel.Endereco,
                IdConheceu=uModel.IdConheceu,
                Senha=uModel.Senha,
                TermosCondicoes=uModel.TermosCondicoes,
                PoliticaPrivacidade=uModel.PoliticaPrivacidade,
                Apelido=uModel.Apelido,
                NomeEmpresaEmp=uModel.NomeEmpresaEmp,
                TelefoneCorporativoEmp=uModel.TelefoneCorporativoEmp,
                EmailCorporativoEmp=uModel.EmailCorporativoEmp,
                SiteEmpr=uModel.SiteEmpr,
                LinkedinEmpr=uModel.LinkedinEmpr,
                InstagramEmp=uModel.InstagramEmp,
                CargoFuncaoEmp=uModel.CargoFuncaoEmp,
                NumeroColaboradoresEmp=uModel.NumeroColaboradoresEmp,
                Cnpj=uModel.Cnpj,
                PlanodeSaudeEmpresa=uModel.PlanodeSaudeEmpresa,
                ContasCorrente=uModel.ContasCorrente,
                BaseImage=uModel.BaseImage,
                BaseImageCompany=uModel.BaseImageCompany
            )

            testtt = empr
        except Exception as e:
            return e

        return empr

    def SintomasEntityToModel(sintomas):
        listsin = []

        for row in sintomas:

            sinn = SintomasVinculadosModel(
                Id=row[0],
                IdSintomaAtendido=row[1],
                IdUsuario=row[2]
            )

            listsin.append(sinn)

        return listsin

    def CartaoEntityToModel(card):
        cartao = CartaoModel(
            Nome=card[0][1],
            Numero=card[0][2],
            Validade=card[0][3],
            IdUsuario=card[0][4]
        )
        return cartao
