# PyCrud
Algoritmo para alterar, buscar, criar e deletar cadastros dentro de um banco de dados local.

<h2><b>REQUISITOS:</b></h2>

<ul>
<li>Primeramente, para poder usar o software, será necessário a instalação do <a href = "https://www.python.org/downloads/">Python</a>, MySQL(abaixo) e Xampp ou semelhantes no PC.</li>

<li>Todos os arquivos <b>devem</b> estar no mesmo diretório (pasta), para que o software possa ser usado. </li>

<li>O Python deve possuir as bibliotecas: <a href="https://tkdocs.com/tutorial/install.html">tkinter (já vem instalado no Windows)</a>, mysql-connector e validate_email</li>
</ul>

<h3><b>Instalando MySQL, Xampp, mysql-connector e validate_email</b></h3>
<ol>
<li>Caso não possua o MySQL e o Xampp, veja o <a href="https://www.youtube.com/watch?v=COepL5-bNNI">vídeo</a> feito pelo Gustavo Guanabara do canal Curso em Vídeo</li>
<li>Para o mysql-connector e o validate_email: vá até a prompt de comando e digite "pip install mysql-connector-python" e depois "pip install validate_email"</li>
</ol>
<h2><b>Como utilizar?</b></h2>

<ol>
<li>Primeiramente, inicie o o arquivo <b>"CRUD.py"</b> para poder iniciar o programa.</li>

<li>Após isso, será mostrado uma janela com os campos de criar, buscar, alterar e deletar.</li>

<li>Para criar um cadastro, vá em Criar, preencha os dados (telefone opcional) e clique em cadastrar. <b>OBS:</b> somente os e-mails válidos e não cadastrados podem ser cadastrados.</li>

<li>Para alterar uma informação em um cadastro já feito, basta preencher o seu e-mail e o dado que será alterado.</li>

<li>Para buscar as informações ou deletar o cadastro, basta ir em Buscar/Deletar e colocar o e-mail alvo.</li>
</ol>