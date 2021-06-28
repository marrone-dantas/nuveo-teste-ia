# Instruções
- As questões devem ser respondidas neste próprio documento `markdown`.
- Quaisquer referências, como papers, páginas web, imagens, etc, podem ser utilizadas para composição das respostas. Porém, é recomendado que as respostas sejam objetivas e diretas.
- Não há uma resposta correta para cada pergunta, de forma que a avaliação não será feita com comparação da resposta fornecida com um gabarito. A ideia da proposta é fornecer a oportunidade de demonstrar o conhecimento na construção de uma solução para o cenário proposto, levantar possíveis limitações, impedimentos e como os problemas podem ser evitados ou minimizados, sem que seja necessário dedicar tempo com experimentos, treinos e determinação de parâmetros de forma empírica.


# Perguntas

1-Explique, de forma objetiva, qual abordagem seria escolhida para solução do problema proposto. Caso a abordagem envolva Redes Neurais, descreva qual seria a arquitetura de rede utilizada e por que.
R: Como estamos tratando de uma problema de classificação, algo que poderíamos fazer seria utilizar uma rede convolucional para classificar as imagens. As assinaturas possuem uma clara distinção de ``foreground e background ``, então a adição de alguma técnica de pre processamento para binarizar a imagem pode ser proveitosa. Com relação a rede poderíamos utilizar algum tipo de transfer-learning, já que possuímos poucos dados, talvez baseado na MNIST, que tem um padrão similar a assinatura. Como complemento, poderíamos gerar uma rede mista, que além da assinatura com entrada contaria com adição de algumas features importantes, de visão computacional clássica, como um array de bordas detectadas, disposição do histograma de cores, transformadas entre outros. 

2-Liste e explique qual a linguagem, framework, pacotes e ferramentas seriam utilizados para construção da solução.
R: Atualmente estou mais familiarizado com Keras com back Tensorflow, seria a ferramenta para gerar o modelo e treinar, assim como Numpy e Pandas para lidar com os dados tabulares. OpenCV para tratamentos de imagens diretamente. Sendo todos esse pacotes utilizados em Python, assim como uma possível deploy para prova de conceito com Flask. 

3-Quais os principais parâmetros da solução e como melhor otimizar a escolha de tais parâmetros?
R: Podemos tentar melhorar os resultados através de um levantamento com grid search. Poderíamos tentar otimizar as dimensões da rede, assim como ativações, otimizadores e funções de loss. 

4-Quais limitações podem impactar a solução proposta, seja em relação à própria abordagem escolhida ou em relação ao dataset fornecido para treino e teste?
R: A base de dados é dividida em assinaturas reais, forjadas e que foram forjadas pelo próprio autor. Existem várias considerações. Se as que forem geradas pelo próprio autor forem consideradas válidas, então teremos uma base mais complexa, onde teremos diversos casos de assinaturas válidas. Treinar uma rede somente com as assinaturas reais aparenta ser menor e complexo. Unir no conjunto de assinaturas válidas (reais + forjadas pelo autor) pode gerar um modelo mais genérico, mesmo que dificulte o treinamento. 

5-Qual seria o prazo proposto para o desenvolvimento da solução proposta?
R: Acredito que para o desenvolvimento de uma solução inicial, o prazo de uma semana seja suficiente. Onde poderíamos analisar as inferências iniciais, tratamento de base, comunicação com o autor, métricas e avaliações. 

6-Considerando um cenário real de uso do método desenvolvido para detecção de fraudes em assinatura, o erro mais prejudicial seria retornar que uma assinatura é legítima quando trata-se de uma assinatura forjada. Como minimizar este tipo de erro?
R: Um dos métodos seria um conjunto de classificadores, em que somente com a opinião de todos conseguimos tomar uma decisão. Outra possibilidade é a adição de exemplos reais e forjados na base, para gerarmos um campo de decisão maior, durante o treinamento deveriamos analisar métrica complementares com taxa de true positive e true negative, para garantir que o modelo tem um eficiência boa relacionada a true positives, ou seja, quando ele afirma que assinatura é verdadeira, tem um confiabilidade maior.  

7-O que poderia ser alterado na disposição de dados para auxiliar o resultado da solução proposta?
R: Acredito que uma união dos dados de treino, transformando em um problema binário, onde somente teríamos duas classes, isso ajudaria no treino e validação. Em algum nível talvez a adição de imagens segmentadas no treino pudesse adicionar informações consideráveis. A base de dados é desbalanceada, como poucos exemplos da assinatura genuína, o que poderia gera um viés. Data augmentation é complexo nesses casos, já que uma simples nuances poderia invalidar uma assinatura, acredito que desde que a forma não fosse modificada, seria uma modificação válida, como brilho, temperatura, leve rotação, entre outros. 
