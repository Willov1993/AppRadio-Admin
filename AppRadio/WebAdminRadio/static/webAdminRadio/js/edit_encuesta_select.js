
var selectbox = document.getElementById('emisoraSelect');
var opts = selectbox.options;

for (var opt, j = 0; opt = opts[j]; j++) {
    if (opt.value == e_emisora) {
        selectbox.selectedIndex = j;
        break;
    }
}

selectbox = document.getElementById('segmentoSelect');
var opts = selectbox.options;
for (var opt, j = 0; opt = opts[j]; j++) {
    if (opt.value == e_segmento) {
        selectbox.selectedIndex = j;
        break;
    }
}

encuesta_component.$data.preguntas.pop()
for (var i = 0; i < list_preguntas.length; i++) {
    encuesta_component.$data.preguntas.push(list_preguntas[i]);
}
encuesta_component.$data.length = list_preguntas.length;