from app.model.usuarioModel import UsuarioModel
from app.entity.usuarioEntity import UsuarioEntity
from app.entity.profissionalEntity import ProfissionalEntity
from app.entity.dependetesEntity import DependentesEntity
from app.entity.empresaEntity import EmpresaEntity

class UsuarioFactory():

    def UsuarioModelToEntity(uModel: UsuarioModel):
        user = UsuarioEntity(
            Nome=uModel.Nome,
            Telefone=uModel.Telefone,
            Email=uModel.Email,
            Cidade=uModel.Cidade,
            Estado=uModel.Estado,
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
            Dependente=uModel.Dependente
        )

        return user

    def ProfissionalModelToEntity(uModel: UsuarioModel):

        try:
            prof = ProfissionalEntity(
                Nome=uModel.Nome,
                Telefone=uModel.Telefone,
                Email=uModel.Email,
                Cidade=uModel.Cidade,
                Estado=uModel.Estado,
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
                CnPj=uModel.CnPj,
                CartaApresentacaoProf=uModel.CartaApresentacaoProf,
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
                ContasCorrente=uModel.ContasCorrente
            )

        except Exception as e: 
            return e

        # if len(uModel.Dependentes) > 0:
        #     for emp in uModel.Dependentes:
        #         nome = emp.Nome
        # else:
        #     print('Nao tem')

        return prof

    def EmpresaModelToEntity(uModel: UsuarioModel):
        
        try:
            empr = EmpresaEntity(
                Nome=uModel.Nome,
                Telefone=uModel.Telefone,
                Email=uModel.Email,
                Cidade=uModel.Cidade,
                Estado=uModel.Estado,
                IdConheceu=uModel.IdConheceu,
                Senha=uModel.Senha,
                TermosCondicoes=uModel.TermosCondicoes,
                PoliticaPrivacidade=uModel.PoliticaPrivacidade,
                Apelido=uModel.Apelido,
                NomeEmpresaEmp = uModel.NomeEmpresaEmp,
                TelefoneCorporativoEmp = uModel.TelefoneCorporativoEmp,
                EmailCorporativoEmp = uModel.EmailCorporativoEmp,
                SiteEmpr = uModel.SiteEmpr,
                LinkedinEmpr = uModel.LinkedinEmpr,
                InstagramEmp = uModel.InstagramEmp,
                CargoFuncaoEmp = uModel.CargoFuncaoEmp,
                NumeroColaboradoresEmp = uModel.NumeroColaboradoresEmp,
                PlanodeSaudeEmpresa = uModel.PlanodeSaudeEmpresa,
                ContasCorrente=uModel.ContasCorrente
            )

            testtt = empr
        except Exception as e: 
            return e

        return empr