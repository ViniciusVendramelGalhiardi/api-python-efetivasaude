from pydantic import BaseModel, json


#translator = google_translator()

class Response(BaseModel):
    status: int
    mensagem: str
    conteudo: str
 
def getResponse(status, mensagem, conteudo):
    #translateMs = translator.translate(mensagem , lang_src='en',  lang_tgt='pt')  
    response_object = Response(
        status=status,
        mensagem= mensagem, #translateMs  if translateMs != None else '',
        conteudo=conteudo, 
    ) 
    return response_object