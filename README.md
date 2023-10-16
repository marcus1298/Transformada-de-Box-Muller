# Transformada-de-Box-Muller
Este projeto tem como objetivo implementar a Transformada de Box-Muller, uma técnica utilizada para gerar números aleatórios que sigam uma distribuição normal (gaussiana). A distribuição normal é fundamental em estatísticas e em muitas áreas da matemática e ciência.

A função principal do projeto pode ser dividida em algumas etapas:

Geração de Números Aleatórios Uniformemente Distribuídos:

Utilizando um gerador de números pseudoaleatórios (nesse caso, o NumPy), são gerados um milhão de pontos aleatórios uniformemente distribuídos.
Aplicação da Transformada de Box-Muller:

A Transformada de Box-Muller é aplicada a esses números uniformemente distribuídos para transformá-los em números normalmente distribuídos.
Visualização da Distribuição:

Um histograma é criado a partir dos números resultantes da Transformada de Box-Muller. O histograma deve exibir um comportamento de distribuição normal.
Essa implementação pode ser usada para gerar dados que seguem uma distribuição normal, o que é útil em simulações, modelagem estatística e em muitas outras aplicações.

A geração de números normalmente distribuídos é crucial em diversas áreas, como finanças, física, aprendizado de máquina e simulação de sistemas complexos. O projeto, assim, fornece uma ferramenta básica para realizar essa transformação e visualizar os resultados.


# Instruções:

# Box-Muller Transform Project

Este projeto implementa a Transformada de Box-Muller para gerar números aleatórios normalmente distribuídos a partir de números aleatórios uniformemente distribuídos.

## Instruções de Uso

1. **Instalação de Dependências:**
   Certifique-se de ter o Python instalado. Você pode instalar as dependências necessárias executando:

   ```bash
   pip install numpy matplotlib
Execução do Código:
Execute o arquivo Python box_muller_transform.py para gerar pontos usando a Transformada de Box-Muller:

bash

python box_muller_transform.py
Resultado:
O programa gerará um gráfico do histograma dos valores obtidos após a transformada, que deverá se assemelhar a uma distribuição normal.

Parâmetros Ajustáveis:
Você pode ajustar o número de pontos gerados e outros parâmetros diretamente no código-fonte.

Contribuições
