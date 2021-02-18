---
layout: page
title: Portfólio
permalink: /Portfolio/
---

# Em construção!


{% for file in site.static_files %}
  {% if file.image %}
<img src="{{file.path}}" alt="{file.name}" style="width:150px">
  {% endif %}
{% endfor %}


### Por enquanto, acesse minha página do GitHub para ver alguns projetos de estudos, meu currículo e meus contatos :

[https://rodrigo-br.github.io/](https://rodrigo-br.github.io/)