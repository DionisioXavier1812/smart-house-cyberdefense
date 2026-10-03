# Ambiente 2 – Intrusão em Smart Lock

## Sobre o Cenário

Fechadura inteligente controlada via aplicativo e painel web, integrada ao hub de automação.

## Arquitetura

- Smart Lock conectada à rede IoT.
- Painel de controle via web/app.
- Hub de automação registrando eventos de abertura/fechamento.
- Logs centralizados.

## Cadeia de Ataque

1. Descoberta do painel de controle.
2. Exploração de credenciais fracas.
3. Acesso ao painel.
4. Comando de destravar a fechadura.
5. Possível acesso físico à residência.

## Incidente

Atacante destrava a fechadura inteligente remotamente.

## Impacto

- Comprometimento de segurança física.
- Risco de invasão domiciliar.
- Exposição de bens materiais e pessoas.

## Logs Simulados

- Login suspeito no painel.
- Comando de destravar em horário incomum.
- IP de origem desconhecido.
- Falhas de login anteriores.

## Indicadores de Comprometimento (IoCs)

- IP de origem.
- Horário de comando.
- User-agent.
- Endpoint de API utilizado.

## MITRE ATT&CK

- T1078 – Valid Accounts
- T1059 – Command Execution
- T1021 – Remote Services

## Timeline DFIR

- T1 – Detecção de comando suspeito.
- T2 – Verificação de origem do acesso.
- T3 – Análise de histórico de logins.
- T4 – Confirmação de acesso indevido.
- T5 – Contenção (revogar acesso, alterar credenciais).

## Evidências

- Logs de comando de destravar.
- Logs de autenticação.
- Registros de API.

## Playbook

1. Identificar comando suspeito.
2. Verificar IP e contexto.
3. Alterar credenciais da Smart Lock.
4. Revisar permissões de acesso.
5. Registrar incidente e reforçar políticas.

## Lições Aprendidas

- Dispositivos físicos conectados exigem segurança máxima.
- Logs de comando devem ser monitorados em tempo real.
- Credenciais fracas são inaceitáveis em dispositivos críticos.

## Recomendações

- MFA quando possível.
- Senhas fortes.
- Monitoramento contínuo.
- Alertas em tempo real para comandos críticos.
