# Matriz de mudanças normativas sobre o STF (1890–2023)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24233241.svg)](https://doi.org/10.5281/zenodo.24233241)

Base de dados que acompanha o artigo **"A personalização do STF como trajetória institucional"**, de Igor Francisco Cavalcanti Nogueira (PPGD/UnB).

A matriz registra 70 mudanças nas regras sobre o Supremo Tribunal Federal entre 1890 e 2023: constituições, emendas constitucionais, leis, o decreto que instituiu o tribunal e o Regimento Interno do STF (textos de 1970 e 1980 e emendas regimentais até a ER 59/2023). Cada mudança é codificada em quatro dimensões, e cada código remete ao dispositivo e ao trecho da norma que o fundamenta.

## Conteúdo

| Arquivo | O que contém |
|---|---|
| `dados/matriz_stf_v10.xlsx` | Planilha completa, com as cinco abas abaixo. É o arquivo de referência. |
| `dados/csv/matriz.csv` | Uma linha por mudança normativa (70 linhas), com os códigos sugeridos, as justificativas e os códigos validados. |
| `dados/csv/evidencias.csv` | Os dispositivos extraídos de cada norma, com texto, situação (original, incluído, alterado, revogado, incerto) e link para a fonte. |
| `dados/csv/dicionario.csv` | Definição de cada variável e de cada código, e o histórico de versões da base. |
| `dados/csv/pendencias.csv` | Dúvidas registradas durante a codificação e como cada uma foi resolvida. |
| `dados/csv/notas_metodologicas.csv` | Decisões de método que afetam a base, como o ponto de partida no Regimento de 1970 e as exclusões por falta de fonte primária. |

Os CSV estão em UTF-8, separados por vírgula. Para abrir no Excel, prefira o `.xlsx`: alguns códigos começam com o sinal `=`, que o Excel tenta ler como fórmula quando importa um CSV.

## Variáveis principais

Cada mudança é codificada em quatro dimensões, com os valores ↑ (ampliou), ↓ (restringiu), ↑↓ (misto), = (manteve) e n/a (não se aplica):

- **V1, competências:** mudou o que o STF pode julgar?
- **V2, acesso:** mudou quem pode levar casos ao tribunal, e por quais filtros?
- **V3, poderes individuais:** mudou o que um ministro pode decidir ou determinar sozinho? A coluna `V3_intensidade` separa os poderes fortes (decidir o mérito ou o destino de uma classe inteira de processos) dos leves (situações específicas, incidentes ou etapas do procedimento).
- **V4, deliberação e publicidade:** mudou como a corte decide ou aparece para o público?

Há ainda quatro variáveis de leitura: `A1` (sentido geral da mudança: individual, coletivo, misto, neutro ou condições), `A2` (dimensão da personalização), `A3` (autoria formal: Constituinte, Congresso, STF ou outro) e `A4` (contexto). As definições completas estão no dicionário.

## Como a base foi construída

As fontes são as páginas oficiais do Planalto, para constituições, emendas e leis, e a edição oficial consolidada do Regimento Interno do STF, para as emendas regimentais. O Regimento de 1970 foi lido no texto original publicado no *Diário da Justiça* de 4 de setembro de 1970.

A extração e a codificação tiveram apoio de inteligência artificial generativa e de scripts, sob três controles. Todo código sugerido traz o dispositivo de onde decorre e a transcrição do trecho; sem dispositivo citado, não há código. Um script confere a planilha e aponta códigos fora do padrão, justificativas ausentes e incoerências entre colunas, sem decidir nada. Por fim, o pesquisador conferiu cada sugestão contra o texto da norma, e só os códigos validados (colunas `*_validado`) compõem a versão final. As colunas `*_sugestao` e `*_justificativa` foram mantidas por transparência e não devem ser lidas como resultado.

O critério de inclusão é restritivo: só entra na base o que foi lido na fonte primária. Os limites que decorrem disso estão nas notas metodológicas e nas pendências.

## Como citar

> NOGUEIRA, Igor Francisco Cavalcanti. *Matriz de mudanças normativas sobre o STF (1890–2023)*. Versão 10. [S. l.]: Zenodo, 2026. Base de dados. DOI: 10.5281/zenodo.24233241. Disponível em: https://doi.org/10.5281/zenodo.24233241.

O DOI 10.5281/zenodo.24233241 identifica a versão 10. Para citar a base sem fixar uma versão, use o DOI 10.5281/zenodo.24233240, que sempre aponta para a mais recente. O artigo correspondente ainda não foi publicado; a referência será acrescentada aqui.

## Licença

Os dados estão disponíveis sob a licença [Creative Commons Atribuição 4.0 Internacional (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.pt-br): podem ser usados, adaptados e redistribuídos, inclusive para fins comerciais, desde que a autoria seja citada. Os textos normativos reproduzidos na aba de evidências são atos oficiais e não estão sujeitos a direitos autorais (Lei nº 9.610/1998, art. 8º, IV).
