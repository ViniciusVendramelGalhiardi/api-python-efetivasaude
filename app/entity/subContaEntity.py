class SubContaEntity:
    Id: str
    IdSubConta: str
    Nome: str
    TokenPrd: str
    TokenDev: str
    TokenUsuario: str
    ComissaoBankSplipCents: str
    ComissaoBankSplipPorcentagem: str
    DataCriacao:str
    ValorComissao: str
    ComissaoCartaoCredito: str
    PorcentagemCartaoCredito: str
    IdComissao: str
    PercentualFixo: str
    PermiteAgregados: str
    ComissaoPix: str
    ComissaoPixPorcentagem: str
    TokenContaReceptador: str
    SplitId: str
    UltimaAtualizacao: str
    IdUsuarioIugu: str
    StatusConta: str

    def __init__(self, Id: str, IdSubConta: str, Nome: str, TokenPrd: str, TokenDev: str, TokenUsuario: str, ComissaoBankSplipCents: str, ComissaoBankSplipPorcentagem: str, 
    DataCriacao:str, ValorComissao: str, ComissaoCartaoCredito: str, PorcentagemCartaoCredito: str, IdComissao: str, PercentualFixo: str, PermiteAgregados: str,
    ComissaoPix:str,ComissaoPixPorcentagem:str,TokenContaReceptador:str,SplitId:str, UltimaAtualizacao:str, IdUsuarioIugu: str, StatusConta:str) -> None:
        self.Id = Id
        self.IdSubConta = IdSubConta
        self.Nome = Nome
        self.TokenPrd = TokenPrd
        self.TokenDev = TokenDev
        self.TokenUsuario = TokenUsuario
        self.ComissaoBankSplipCents = ComissaoBankSplipCents
        self.ComissaoBankSplipPorcentagem = ComissaoBankSplipPorcentagem
        self.DataCriacao = DataCriacao
        self.ValorComissao = ValorComissao
        self.ComissaoCartaoCredito = ComissaoCartaoCredito
        self.PorcentagemCartaoCredito = PorcentagemCartaoCredito
        self.IdComissao = IdComissao
        self.PercentualFixo = PercentualFixo
        self.PermiteAgregados = PermiteAgregados
        self.ComissaoPix = ComissaoPix
        self.ComissaoPixPorcentagem = ComissaoPixPorcentagem
        self.TokenContaReceptador = TokenContaReceptador
        self.SplitId = SplitId
        self.UltimaAtualizacao = UltimaAtualizacao
        self.IdUsuarioIugu = IdUsuarioIugu
        self.StatusConta = StatusConta