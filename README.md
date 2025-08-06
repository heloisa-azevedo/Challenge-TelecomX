<h1 align="center">📉 Análise de Evasão de Clientes (Churn) - TelecomX</h1>
<p align="center">
Este projeto foi desenvolvido durante meus estudos no <strong>Programa ONE - Oracle Next Education</strong>.
</p>

<h2>💡 Objetivo</h2> 
<p>
O objetivo deste projeto foi compreender os fatores associados à <strong>evasão de clientes (churn)</strong>, analisando variáveis como tipo de contrato, tempo de permanência, método de pagamento, entre outras. A partir da análise, foram gerados insights para sugerir <strong>ações estratégicas de retenção</strong>.
</p>

<h2>🛠️ Ferramentas Utilizadas</h2>
<ul>
  <li>Python</li>
  <li>Pandas</li>
  <li>NumPy</li>
  <li>Matplotlib</li>
  <li>Seaborn</li>
  <li>VS Code (com Jupyter extension)</li>
</ul>

<h1>📈 Análises Realizadas</h1>

<h2>📊 Distribuição Geral do Churn</h2>
<p align="center"><em><img src="https://github.com/heloisa-azevedo/Challenge-TelecomX/blob/main/img/graf1%20-%20Distribui%C3%A7%C3%A3o%20de%20Churn.png"></em></p>
<p align="center"><em><img src="https://github.com/heloisa-azevedo/Challenge-TelecomX/blob/main/img/graf2%20-%20Propor%C3%A7%C3%A3o%20de%20Churn.png"></em></p>
<p><strong>Análise:</strong><br>
A evasão representa 96,9% da base de clientes, mostrando que a maior parte dos usuários cancela os serviços. Essa proporção extrema é um indicativo de que estratégias de fidelização podem estar falhando.
</p>

<h2>👥 Churn por Gênero</h2>
<p align="center"><em><img src="https://github.com/heloisa-azevedo/Challenge-TelecomX/blob/main/img/graf3%20-%20Propor%C3%A7%C3%A3o%20de%20Churn%20por%20G%C3%AAnero.png"></em></p>
<p><strong>Análise:</strong><br>
A diferença entre os gêneros é pequena: 97,1% das mulheres e 96,7% dos homens evadiram. O gênero não parece ser um fator determinante para o churn.
</p>

<h2>📄 Churn por Tipo de Contrato</h2>
<p align="center"><em><img src="https://github.com/heloisa-azevedo/Challenge-TelecomX/blob/main/img/graf4%20-%20Total%20de%20Clientes%20que%20evadiram%20por%20Tipo%20de%20Contrato.png"></em></p>
<p><strong>Análise:</strong><br>
Clientes com contrato mensal foram os que mais cancelaram (3.875 casos), seguidos por contratos de dois anos (1.695) e um ano (1.473). Isso indica que contratos mais curtos aumentam a probabilidade de evasão.
</p>

<h2>💳 Churn por Método de Pagamento</h2>
<p align="center"><em><img src="https://github.com/heloisa-azevedo/Challenge-TelecomX/blob/main/img/graf5%20-%20Total%20de%20Clientes%20que%20evadiram%20por%20M%C3%A9todo%20de%20Pagamento.png"></em></p>
<p><strong>Análise:</strong><br>
Clientes que pagam via <strong>Electronic Check</strong> apresentaram maior evasão (2.365 casos), o que pode estar ligado à falta de praticidade ou baixa fidelização associada a esse método.
</p>

<h2>🌐 Churn por Tipo de Serviço de Internet</h2>
<p align="center"><em><img src="https://github.com/heloisa-azevedo/Challenge-TelecomX/blob/main/img/graf6%20-%20N%C3%BAmero%20de%20Clientes%20que%20evadiram%20por%20Tipo%20de%20Servi%C3%A7o%20de%20Internet.png"></em></p>
<p><strong>Análise:</strong><br>
Clientes com <strong>Fiber optic</strong> lideram o churn (3.096 casos), mesmo sendo um serviço considerado premium. DSL vem em seguida (2.421), e até mesmo quem não possui internet (1.526) apresenta evasão, o que pode apontar para outras causas além da qualidade do serviço.
</p>

<h2>💰 Total Gasto × Churn</h2>
<p align="center"><em><img src="https://github.com/heloisa-azevedo/Challenge-TelecomX/blob/main/img/graf7%20-%20Total%20Gasto%20por%20Churn.png"></em></p>
<p><strong>Análise:</strong><br>
A mediana do gasto total é maior entre os clientes que evadiram. Isso pode indicar uma percepção negativa de custo-benefício ou insatisfação mesmo entre os que mais gastam.
</p>

<h2>📆 Tempo de Contrato × Churn</h2>
<p align="center"><em><img src="https://github.com/heloisa-azevedo/Challenge-TelecomX/blob/main/img/graf8%20-%20Tempo%20de%20Contrato%20por%20Churn.png"></em></p>
<p><strong>Análise:</strong><br>
Clientes que permaneceram possuem tempo de contrato ligeiramente maior que os que cancelaram, reforçando que <strong>clientes mais antigos tendem a ser mais fiéis</strong>.
</p>

<h2>🏁 Conclusão</h2>
<p>
As análises mostraram que o churn está mais relacionado a <strong>características contratuais e comportamentais</strong> do que a variáveis demográficas como gênero. Contratos curtos, métodos de pagamento manuais e menor tempo de permanência se mostraram indicadores importantes de risco de evasão.
</p>
<p>
<strong>Recomendações:</strong><br>
- Implementar programas de fidelidade para contratos mensais;<br>
- Incentivar métodos de pagamento automáticos;<br>
- Oferecer suporte e benefícios personalizados para clientes novos ou de alto valor;<br>
- Avaliar a experiência de usuários com internet fibra, buscando entender causas de insatisfação.
</p>

