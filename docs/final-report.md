# Final Report – Smart House CyberDefense

## Resumo
Incidente envolvendo três dispositivos IoT: câmera IP, Smart Lock e assistente de voz.

## Achados
- Credenciais fracas  
- API exposta  
- Comandos críticos sem proteção  
- Pivoting entre dispositivos IoT  

## Timeline Consolidada
11:22 – Login suspeito na câmera  
11:23 – Unlock remoto no Smart Lock  
11:24 – Comando malicioso via assistente de voz  

## Evidências
- auth.log  
- smartlock.log  
- assistant.log  
- pcap de tráfego  

## Análise DFIR
Atacante explorou credenciais fracas, APIs expostas e permissões excessivas.

## Conclusão
Ambientes domésticos com IoT exigem segurança corporativa.

## Recomendações
- MFA  
- Hardening IoT  
- Segmentação  
- Monitoramento contínuo  
