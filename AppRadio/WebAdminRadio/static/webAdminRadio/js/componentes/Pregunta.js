/* -- Componente Preguntas -- 
    Este componente crea las preguntas para el concurso
*/

const Pregunta = {
    data() {
        return{
           preguntas:[]
        }
    },
    methods: {
        agregarPregunta(){
            this.preguntas.push({
                'descripcion': null
            })
        },
        eliminarPregunta(indice){
            this.preguntas.splice(indice, 1)
        }
    },
    mounted(){
        this.agregarPregunta()
    },
    template:/*html*/`
    <div>
        <div v-for="(pregunta, index) in preguntas" v-bind:key="index" class="form-row">
            <div class="form-group col-md-4">
                <span>Preguntas:</span>
                <label for="preguntaInput">Agregue las preguntas para su concurso</label>
                <input required name="pregunta" id="preguntaInput" type="text" class="form-control" placeholder="Ingrese pregunta" maxlength=150>
                <label for="respuestaInput">Respuesta:</label>
                <input required name="pregunta" id="preguntaInput" type="text" class="form-control" placeholder="Opcion" maxlength=150>
                <button type="button" class="btn btn-primary" id="addHorario" @click="agregarPregunta">Agregar pregunta</button>
                <div class="form-group col-md-3" id="btn-eliminar-div">
                    <div id="btn-eliminar"">
                        <button type="button" class="btn btn-primary" id="addHorario" @click="eliminarPregunta">Eliminar</button>
                    </div>
                </div>
            </div>
        </div>
        <button type="button" class="btn btn-primary" id="addHorario" @click="agregarPregunta">Agregar pregunta</button>
    </div>
    `
}

/* Variable contenedora de la instancia del componente horario */
var contenedorPregunta = new Vue({
    el: '#componente_pregunta',
    components: {
        'pregunta': Pregunta
    }
})

