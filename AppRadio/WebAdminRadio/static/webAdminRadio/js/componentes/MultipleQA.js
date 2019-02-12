/* -- Componente de preguntas y respuestas múltiples -- */
Vue.component('encuesta', {
    props: {
        question: String,
        answer: String,
        type: String,
        options: Array,
        size: Number,
        indice: Number,
        esConcurso: Boolean
    },
    template:
    /*html*/`
    <div>
        <div class="form-group col-md-10" >
            <div class="form-group">
                <label for="pregunta"><br><b>Pregunta:</b></label>
                <button v-if="indice > 1" type="button" class="float-right btn btn-primary" @click="eliminar_pregunta">Eliminar Pregunta</button>
            </div>
            <input required type="text" name="preguntas" class="form-control" v-model="question" v-on:input="update(question)">
        </div>
        <div v-if='esConcurso' class="form-group col-md-10" >
            <div class="form-group">
                <label for="tipo"><b>Tipo Pregunta:</b></label>
            </div>
            <select required name="tipo" class="form-control" v-model="type">
                <option value="F" selected>Pregunta de Filtro</option>
                <option value="C"> Pregunta de Concurso</option>
            </select>
        </div>
        <div v-if='esConcurso' class="form-group col-md-10" >
            <div class="form-group">
                <label for="respuesta_correcta"><b>Respuesta correcta:</b></label>
            </div>
            <input required type="text" name="respuesta_correcta" class="form-control" v-model="answer">
        </div>
        <div class="form-group col-md-10">
            <label for="opcion">Respuestas:</label>
            <button type="button" class="float-right btn btn-primary" @click="agregar">Agregar otra opción</button>
        </div>
        <div class="form-row col-md-12" v-for="(opt, index) in options" :key="index">
            <div class="form-group col-md-10">
                <input v-bind:name="'respuesta' + indice" class="form-control" v-model="opt.opcion">
            </div>
            <div class="form-group col-md-1" id="btn-eliminar-div">
                <div id="btn-eliminar">
                    <button v-if="index > 1" @click="eliminar(index)" type="button" class="btn btn-primary" id="eliminar">Eliminar</button>
                </div>
            </div>
        </div>
    </div>
    `,
    methods: {
        eliminar(i) {
            this.$emit('eliminar-opcion', i)
        },
        agregar() {
            this.$emit('agregar-opcion')
        },
        eliminar_pregunta() {
            this.$emit('eliminar-pregunta')
        },
        update(value){
            this.$emit('update-question', value)
        },
        updateCorrecta(value){
            this.$emit('update-correcta', value)
        }
    }
})

encuesta_component = new Vue({
    el: '#componente_pregunta',
    data() {
        return {
            preguntas: [
                {
                    pregunta: null,
                    respuesta: null,
                    tipo: null,
                    opciones: [
                        { opcion: null },
                        { opcion: null },
                    ]
                },
            ],
            length: 1
        }
    },
    methods: {
        agregarPregunta() {
            this.preguntas.push({
                'pregunta': null,
                'respuesta': null,
                'tipo': null,
                'opciones': [
                    { 'opcion': null },
                    { 'opcion': null }
                ]
            });
            this.length++;
        },
        eliminarPregunta(event) {
            this.preguntas.splice(event, 1);
            this.length--;
        },
        eliminarOpcion(event, index) {
            this.preguntas[index].opciones.splice(event, 1);
        },
        agregarOpcion(index) {
            this.preguntas[index].opciones.push({
                'opcion': null
            })
        },
        updatePregunta(event, index) {
            this.preguntas[index].pregunta = event;
        },
        updateCorrecta(event,index){
            this.preguntas[index].respuesta= event;
        }
    }
})