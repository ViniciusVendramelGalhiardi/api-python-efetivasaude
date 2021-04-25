from typing import  Optional

class Errors:
    pass
    def __init__(self, ) -> None:
        pass

class ResponsePagamentoModel:
    status: Optional[str]
    info_message: Optional[str]
    reversible: Optional[str]
    token: Optional[str]
    brand: Optional[str]
    bin: Optional[str]
    success: Optional[str]
    url: Optional[str]
    pdf: Optional[str]
    identification: Optional[str]
    invoice_id: Optional[str]
    lr: Optional[str]

    def __init__(self, status: Optional[str],  info_message: Optional[str], reversible: Optional[str], token: Optional[str],
         brand: Optional[str], bin: Optional[str], success: Optional[str], url: Optional[str], pdf: Optional[str], identification: Optional[str], 
         invoice_id: Optional[str], lr: Optional[str]) -> None:
        self.status = status
        self.info_message = info_message
        self.reversible = reversible
        self.token = token
        self.brand = brand
        self.bin = bin
        self.success = success
        self.url = url
        self.pdf = pdf
        self.identification = identification
        self.invoice_id = invoice_id
        self.lr = lr
