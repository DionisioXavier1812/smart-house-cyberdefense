# Ambiente 2 – Smart Lock

Descrição:
Fechadura controlada via app.

Arquitetura:
IoT VLAN -> SmartLock -> Hub

Cadeia:
1 painel descoberto
2 credenciais fracas
3 unlock remoto

Incidente:
Destravamento indevido

Impacto:
Risco físico

Logs:
unlock remoto

IoCs:
201.55.19.77

MITRE:
T1059, T1021

Timeline:
T1 unlock

Evidências:
smartlock.log

Playbook:
resetar credenciais

Lições:
MFA

Recomendações:
alertas críticos
