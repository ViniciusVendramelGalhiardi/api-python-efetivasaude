import json
from json import JSONEncoder

class Data:
    brand: str
    holder_name: str
    display_number: str
    bin: int
    year: int
    month: int
    last_digits: int
    first_digits: int
    masked_number: str

    def __init__(self, brand: str, holder_name: str, display_number: str, bin: int, year: int, month: int, last_digits: int, first_digits: int, masked_number: str) -> None:
        self.brand = brand
        self.holder_name = holder_name
        self.display_number = display_number
        self.bin = bin
        self.year = year
        self.month = month
        self.last_digits = last_digits
        self.first_digits = first_digits
        self.masked_number = masked_number


class FormaPagamentoModel:
    id: str
    description: str
    item_type: str
    customer_id: str
    data: Data

    def __init__(self, id: str, description: str, item_type: str, customer_id: str, data: Data) -> None:
        self.id = id
        self.description = description
        self.item_type = item_type
        self.customer_id = customer_id
        self.data = data

class FormaPgtoEntity:
      Id: str
      IdFormaPgtoIugu: str
      DescricaoPgto: str
      TipoFormaPgto: str
      IdUsuarioIugu: str
      BandeiraCartao:str
      NomeCartao: str
      NumeroCartao: str
      Bin: str
      AnoVencimento: str
      Mes: str
      UltimosDigitos:str 
      PrimeirosDigitos: str
      NumeroMascara:str

      def __init__(self, id: str, IdFormaPgtoIugu: str,DescricaoPgto: str, TipoFormaPgto: str, IdUsuarioIugu: str,
       BandeiraCartao: str, NomeCartao: str, NumeroCartao: str, Bin: str,AnoVencimento: str, Mes: str, UltimosDigitos: str,PrimeirosDigitos: str, NumeroMascara: str) -> None:
       self.id = id
       self.IdFormaPgtoIugu = IdFormaPgtoIugu
       self.DescricaoPgto = DescricaoPgto
       self.TipoFormaPgto = TipoFormaPgto
       self.IdUsuarioIugu = IdUsuarioIugu
       self.BandeiraCartao = BandeiraCartao
       self.NomeCartao = NomeCartao
       self.NumeroCartao = NumeroCartao
       self.Bin = Bin
       self.AnoVencimento = AnoVencimento
       self.Mes = Mes
       self.UltimosDigitos = UltimosDigitos
       self.PrimeirosDigitos = PrimeirosDigitos
       self.NumeroMascara = NumeroMascara



class PgtoEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__


def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)