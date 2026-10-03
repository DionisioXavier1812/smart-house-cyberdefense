# Final Report – Smart House CyberDefense

## Resumo Executivo

Este relatório consolida os incidentes simulados em uma residência inteligente, com foco em dispositivos IoT, automação residencial e segurança da informação aplicada ao contexto doméstico.

## Escopo

- Câmera IP comprometida.
- Fechadura inteligente com acesso indevido.
- Assistente de voz abusado para ações não autorizadas.
- Pivoting via dispositivos IoT.

## Metodologia

- Coleta de logs simulados.
- Construção de timeline DFIR.
- Análise de evidências.
- Mapeamento MITRE ATT&CK.
- Recomendações de segurança.

## Principais Achados

- Credenciais fracas em dispositivos IoT.
- Exposição indevida de interfaces de administração.
- Falta de segmentação adequada da rede.
- Ausência de monitoramento contínuo.

## Timeline DFIR (Resumo)

- T0 – Configuração inicial da casa inteligente.
- T1 – Tentativa de acesso remoto à câmera IP.
- T2 – Sucesso na autenticação indevida.
- T3 – Acesso à smart lock via painel web.
- T4 – Execução de comandos via assistente de voz.
- T5 – Detecção de anomalias em logs.
- T6 – Contenção e hardening.

## Recomendações

- Implementar segmentação de rede IoT.
- Aplicar senhas fortes e MFA quando possível.
- Monitorar logs e gerar alertas.
- Atualizar firmware regularmente.
- Revisar políticas de acesso remoto.

## Conclusão

O ambiente de casa inteligente exige o mesmo nível de atenção que ambientes corporativos, especialmente quando dispositivos IoT controlam aspectos físicos da residência.  
Este projeto demonstra, em formato de portfólio, como DFIR, MITRE ATT&CK e Blue Team podem ser aplicados em um cenário doméstico.
