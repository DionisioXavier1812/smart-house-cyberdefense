# Ambiente 1 – Câmera IP Comprometida

## Sobre o Cenário
Câmera IP exposta na VLAN IoT, acessível via painel web sem MFA.

## Arquitetura
Internet ? Router ? VLAN IoT ? Camera-IP ? Hub IoT

## Cadeia de Ataque
1. Descoberta da porta 554 exposta
2. Brute force no painel web
3. Login bem-sucedido
4. Alteração de configuração
5. Acesso ao feed de vídeo

## Incidente
Atacante acessou o painel da câmera e alterou configurações críticas.

## Impacto
Violação de privacidade e exposição de imagens internas.

## Logs Simulados
Oct 03 11:22:14 camera-ip auth: Failed login from 189.22.14.55
Oct 03 11:22:18 camera-ip auth: Successful login
Oct 03 11:23:01 camera-ip system: Configuration changed

## IoCs
IP: 189.22.14.55
User-Agent: Mozilla/5.0 (AttackBot)
URI: /login
Hash: 9f8b2c1d0eaa12f3c4d9a1b2e3f7aa91

## MITRE ATT&CK
T1078 – Valid Accounts
T1040 – Network Sniffing
T1059 – Command Execution

## Timeline DFIR
11:22 – Tentativa de login
11:22 – Login bem-sucedido
11:23 – Alteração de configuração

## Evidências
auth.log
config.log
pcap

## Análise
Atacante explorou credenciais fracas e painel exposto.

## Conclusão
Câmeras IoT exigem hardening e MFA.

## Recomendações
Hardening IoT
Segmentação
MFA
