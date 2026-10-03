# Ambiente 3 – Abuso de Assistente de Voz e Pivoting IoT

## Sobre o Cenário

Assistente de voz integrado à automação residencial, capaz de controlar dispositivos IoT e executar ações na casa.

## Arquitetura

- Assistente de voz conectado à nuvem.
- Integração com hub de automação.
- Controle de dispositivos (luzes, smart lock, câmeras).
- Logs de comandos armazenados.

## Cadeia de Ataque

1. Comprometimento da conta do assistente de voz.
2. Execução de comandos maliciosos (abrir portas, desligar alarmes).
3. Uso de dispositivos IoT como ponto de pivoting.
4. Acesso à rede interna via dispositivos comprometidos.

## Incidente

Atacante usa o assistente de voz para executar ações não autorizadas e pivotar para outros dispositivos.

## Impacto

- Controle indevido da casa.
- Risco físico e digital.
- Exposição de dados e rotinas.

## Logs Simulados

- Comandos incomuns via voz.
- Ações críticas executadas em horários estranhos.
- Integrações IoT acionadas em sequência.
- Eventos de rede associados.

## Indicadores de Comprometimento (IoCs)

- Histórico de comandos.
- IPs de origem da conta.
- Dispositivos acionados em cadeia.
- URIs de APIs utilizadas.

## MITRE ATT&CK

- T1078 – Valid Accounts
- T1059 – Command Execution
- T1041 – Exfiltration Over C2 Channel

## Timeline DFIR

- T1 – Detecção de comandos incomuns.
- T2 – Análise de histórico de ações.
- T3 – Correlação com dispositivos IoT.
- T4 – Identificação de pivoting.
- T5 – Contenção (revogar acesso, redefinir integrações).

## Evidências

- Logs de comandos de voz.
- Logs de automação.
- Registros de dispositivos acionados.

## Playbook

1. Revisar histórico de comandos.
2. Verificar origem da conta comprometida.
3. Revogar sessões ativas.
4. Redefinir credenciais e integrações.
5. Documentar incidente e reforçar segurança.

## Lições Aprendidas

- Assistentes de voz são vetores críticos.
- Integrações IoT devem ser monitoradas.
- Comandos críticos exigem validação adicional.

## Recomendações

- Revisar permissões do assistente de voz.
- Monitorar comandos críticos.
- Aplicar alertas para ações sensíveis.
- Educar usuários sobre riscos.
