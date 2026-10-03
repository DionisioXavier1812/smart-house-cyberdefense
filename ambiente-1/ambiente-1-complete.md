# Ambiente 1 – Câmera IP

Descrição:
Câmera acessível via painel web.

Arquitetura:
IoT VLAN -> Camera -> Hub

Cadeia:
1 brute force
2 login
3 config change

Incidente:
Acesso indevido ao feed

Impacto:
Privacidade comprometida

Logs:
Failed login
Successful login

IoCs:
189.22.14.55

MITRE:
T1078, T1040

Timeline:
T1 login
T2 config change

Evidências:
auth.log

Playbook:
bloquear IP, alterar senha

Lições:
remover credenciais padrão

Recomendações:
hardening
