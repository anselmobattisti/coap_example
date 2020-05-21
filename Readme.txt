Softwares necessários:
----------------------

1 - Python 2.7.16
2 - O Coap Server utilizado foi o CoAPthon versão 4.0.2

>> sudo pip install CoAPthon

Como executar os testes:
----------------------

1 - Para rodar os testes primeiro é necessário estar com o SenseHat aberto 

2 - Rodar o Servidor Coap

>> python server_2.py 127.0.0.1 5683

Aparecerá escrito "Add New Sensor", Digite o ID do sensor, por exmeplo s2; O ID do sensor s1 já foi criado por padrão 

3 - Precisamos insrir um valor no recurso s1 do CoaP Server, abra outro terminar e execute 

>> python sensor_simulator.py -o POST -p coap://127.0.0.1:5683/s1 -P 55

4 - Insira algum valor dentro do s2

>> python sensor_simulator.py -o POST -p coap://127.0.0.1:5683/s2 -P 10

5 -Em um outro terminal rode o script que será o cliente e fará uso do SenseRat

>> python client.py 127.0.0.1 5683 s1 20

Os leds ficarão vermelhos pois o limite que foi setado é de 20 e o valor armazenado no seu resource no CoaP s1 é 55.

6 - Alere o valor do CoaP do recurso s1 para 10

>> python sensor_simulator.py -o POST -p coap://127.0.0.1:5683/s1 -P 10

Os leds deverão ficar brancos

7 - Rode outro simulador mas agora configure para que ele leia os valores armazenados em S2

>> python client.py 127.0.0.1 5683 s2 5

Cada cliente está lendo o seu recurso específico no servidor Coap