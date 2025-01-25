<h1><strong>Python: Aplicando a Orientação a Objetos</strong></h1>

<h2>📜 Sobre o Projeto</h2>
<p>
  Este repositório contém um projeto desenvolvido como parte do curso da Alura 
  <a href="https://cursos.alura.com.br/course/python-aplicando-orientacao-objetos" target="_blank">
    Python: Aplicando Orientação a Objetos
  </a>. 
  O projeto consiste em um sistema para gerenciar restaurantes, permitindo:
</p>
<ul>
  <li>Cadastrar restaurantes com informações como nome, categoria, CNPJ e contato.</li>
  <li>Atribuir avaliações (notas) aos restaurantes.</li>
  <li>Calcular e exibir a média de avaliações de cada restaurante.</li>
  <li>Alterar o status ativo/inativo dos restaurantes.</li>
  <li>Listar os restaurantes cadastrados de forma organizada.</li>
</ul>

<h2>🛠️ Tecnologias Utilizadas</h2>
<ul>
  <li>Python 3.10+</li>
  <li>Paradigma de Orientação a Objetos (POO)</li>
</ul>

<h2>🏗️ Estrutura do Projeto</h2>
<ul>
  <li><strong>Modelos:</strong> Classes que representam os principais elementos do sistema:
    <ul>
      <li><strong>Restaurante:</strong> Gerencia os dados e operações relacionadas aos restaurantes.</li>
      <li><strong>Avaliacao:</strong> Representa as avaliações feitas pelos clientes.</li>
    </ul>
  </li>
  <li><strong>App:</strong> Contém a lógica principal para inicializar o sistema e demonstrar as funcionalidades.</li>
</ul>

<h2>⚙️ Funcionalidades</h2>
<ul>
  <li>Cadastrar novos restaurantes.</li>
  <li>Exibir uma lista detalhada de restaurantes, incluindo:
    <ul>
      <li>Nome, categoria, CNPJ, contato, média de avaliações e status (ativo/inativo).</li>
    </ul>
  </li>
  <li>Adicionar avaliações a restaurantes.</li>
  <li>Calcular a média das avaliações de forma automática.</li>
  <li>Alterar o status de um restaurante entre ativo e inativo.</li>
</ul>

<h2>🚀 Como Executar o Projeto</h2>
<ol>
  <li>Certifique-se de ter o Python 3.10+ instalado em seu computador.</li>
  <li>Clone o repositório para sua máquina local:
    <pre><code>git clone https://github.com/seu-usuario/seu-repositorio.git</code></pre>
  </li>
  <li>Navegue até o diretório do projeto:
    <pre><code>cd seu-repositorio</code></pre>
  </li>
  <li>Execute o arquivo principal:
    <pre><code>python app.py</code></pre>
  </li>
</ol>

<h2>🖼️ Exemplo de Saída</h2>
<p>Abaixo está um exemplo da saída ao listar os restaurantes cadastrados:</p>
<pre>
Nome do restaurante        | Categoria              | CNPJ                   | Contato                | Avaliações            | Status
Pizza                     | PIZZARIA               | 80406087000130         | 121234431256789        | O restaurante ainda não possui nenhuma avaliação | ☐
Dondó                     | COMIDA NORDESTINA      | 82173441000150         | 119080706058           | 2.7                   | ☐
Japonês do amor           | JAPONESA               | 42468159000185         | 1190909005438          | O restaurante ainda não possui nenhuma avaliação | ☑
</pre>
