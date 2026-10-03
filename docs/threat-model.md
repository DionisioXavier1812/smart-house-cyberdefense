# Threat Model – Smart House CyberDefense

## Sobre o Cenário

Residência inteligente com dispositivos IoT, automação residencial, rede segmentada e acesso remoto controlado.  
O foco é avaliar riscos de ataques a dispositivos IoT e à automação da casa.

## Ativos Principais

- Hub de automação residencial
- Câmeras IP
- Fechadura inteligente (Smart Lock)
- Assistente de voz
- Rede doméstica (Wi-Fi / IoT)
- Dados de usuários e histórico de eventos

## Adversários

- Atacante externo com foco em IoT.
- Atacante oportunista explorando credenciais fracas.
- Atacante com acesso à rede doméstica (visitante malicioso).

## Superfícies de Ataque

- Exposição de portas e serviços IoT.
- Painéis de administração de câmeras e smart lock.
- APIs de automação residencial.
- Assistente de voz conectado à nuvem.

## Vetores de Ataque

- Credenciais fracas ou reutilizadas.
- Exploração de vulnerabilidades em firmware.
- Ataques de força bruta em interfaces web.
- Phishing para obter acesso à conta de automação.

## Mitigações

- Senhas fortes e únicas.
- Atualização de firmware.
- Segmentação de rede IoT.
- Monitoramento de logs e alertas.
- Hardening de dispositivos.

## Severidade

- Comprometimento de privacidade (câmeras).
- Comprometimento de segurança física (smart lock).
- Exposição de hábitos e rotinas (assistente de voz).
