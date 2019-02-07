/* -- Componente de preguntas y respuestas múltiples -- */
Vue.component('encuesta', {
    props: ['question', 'options', 'size', 'indice'],
    template:
    /*html*/`
    <div>
        <div class="form-group col-md-10" >
            <div class="form-group">
                <label for="pregunta">Pregunta:</label>
                <button v-if="size > 1" type="button" class="float-right btn btn-primary" @click="eliminar_pregunta">Eliminar Pregunta</button>
            </div>
            <input required type="text" name="preguntas" class="form-control" v-model="question" v-on:input="update(question)">
        </div>
        <div class="form-group col-md-10">
            <label for="opcion">Respuestas:</label>
            <button type="button" class="float-right btn btn-primary" @click="agregar">Agregar otra opción</button>
        </div>
        <div class="form-row col-md-12" v-for="(opt, index) in options" :key="index">
            <div class="form-group col-md-10">
                <input required v-bind:name="'respuesta' + indice" class="form-control" v-model="opt.opcion">
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
        }
    }
})