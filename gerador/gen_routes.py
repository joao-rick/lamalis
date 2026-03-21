from fastapi import APIRouter
from generator import geraCoin, geraValorAtual, geraValorInicial, geraNivelRisco, geraSigla

gen_router = APIRouter(prefix="/v1", tags=["generator"])

@gen_router.get("/cripto")
async def generate_cripto():
	coin_gerada = geraCoin()
	nome_criptomoeda = "".join(coin_gerada[0])

	return {
		"nome_criptomoeda": nome_criptomoeda,
		"sigla": geraSigla(nome_criptomoeda),
		"valor_atual": geraValorAtual(),
		"valor_inicial": geraValorInicial(),
		"nivel_risco": geraNivelRisco(),
	}
