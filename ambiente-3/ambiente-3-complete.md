# Ambiente 3 – Assistente de Voz

Descrição:
Assistente integrado ao hub.

Arquitetura:
Hub -> VoiceAssistant -> IoT

Cadeia:
1 conta comprometida
2 comandos maliciosos
3 pivoting

Incidente:
Ações indevidas

Impacto:
Controle da casa

Logs:
unlock via voz

IoCs:
comando suspeito

MITRE:
T1041, T1059

Timeline:
T1 comando

Evidências:
assistant.log

Playbook:
revogar sessões

Lições:
alertas de voz

Recomendações:
hardening IoT
