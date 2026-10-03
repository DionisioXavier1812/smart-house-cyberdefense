# Ambiente 1 – Comprometimento de Câmera IP

## Sobre o Cenário

Câmera IP instalada na residência, acessível via painel web, com acesso remoto habilitado.

## Arquitetura

- Câmera IP conectada à rede IoT.
- Painel web acessível via HTTP/HTTPS.
- Hub de automação registrando eventos.
- Logs armazenados em sistema central.

## Cadeia de Ataque

1. Descoberta da câmera via varredura de rede.
2. Tentativa de login com credenciais padrão.
3. Sucesso na autenticação indevida.
4. Acesso ao feed de vídeo.
5. Alteração de configurações.

## Incidente

Atacante obtém acesso à câmera IP e visualiza o interior da residência.

## Impacto

- Violação de privacidade.
- Exposição de rotina da família.
- Possível apoio a crimes físicos.

## Logs Simulados

- Tentativas de login falhas.
- Login bem-sucedido de IP suspeito.
- Alteração de configurações.
- Acesso ao feed em horários incomuns.

## Indicadores de Comprometimento (IoCs)

- IP de origem desconhecido.
- User-agent incomum.
- URLs de acesso ao painel.
- Horários de acesso fora do padrão.

## MITRE ATT&CK

- T1078 – Valid Accounts
- T1040 – Network Sniffing
- T1021 – Remote Services

## Timeline DFIR

- T1 – Detecção de login suspeito.
- T2 – Correlacionar IP com outros eventos.
- T3 – Verificar alterações de configuração.
- T4 – Confirmar acesso indevido.
- T5 – Contenção (alterar credenciais, bloquear IP).

## Evidências

- Logs de autenticação.
- Logs de configuração.
- Registros de acesso ao painel.

## Playbook

1. Identificar IP suspeito.
2. Bloquear IP no firewall.
3. Alterar credenciais da câmera.
4. Revisar configurações de acesso remoto.
5. Registrar incidente e lições aprendidas.

## Lições Aprendidas

- Nunca usar credenciais padrão.
- Monitorar acessos remotos.
- Aplicar hardening em dispositivos IoT.

## Recomendações

- Senhas fortes e únicas.
- Atualização de firmware.
- Restrição de acesso remoto.
- Monitoramento contínuo de logs.
