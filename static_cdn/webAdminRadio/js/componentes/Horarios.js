/* -- Componente Horarios -- 
    Este componente crea los elemetos de día para agregar más días a los horarios
    de los segmentos
*/

const Horario = {
    data() {
        return{
            horarios:[]
        }
    },
    methods: {
        agregarDia(){
            this.horarios.push({
                'dia': null,
                'inicio': null,
                'fin': null
            })
        },
        eliminarDia(indice){
            this.horarios.splice(indice, 1)
        }
    },
    mounted(){
        this.agregarDia()
    },
    template:/*html*/`
    <div>
        <div v-for="(horario, index) in horarios" v-bind:key="index" class="form-row">
            <div class="form-group col-md-3">
                <label>Dia</label>
                <select v-model="horario.dia" v-bind:name="'dia' + (index + 1)" id="diaInput" class="custom-select form-control" required>
                    <option value="Lunes">Lunes</option>
                    <option value="Martes">Martes</option>
                    <option value="Miércoles">Miércoles</option>
                    <option value="Jueves">Jueves</option>
                    <option value="Viernes">Viernes</option>
                </select>
            </div>
            <div class="form-group col-md-3">
                <label>Hora de inicio</label>
                <input v-model="horario.inicio" v-bind:name="'inicio' + (index + 1)" type="time" class="form-control" required>
            </div>
            <div class="form-group col-md-3">
                <label>Hora fin</label>
                <input v-model="horario.fin" v-bind:name = "'fin' + (index + 1)" type="time" class="form-control" required>
            </div>
            <div class="form-group col-md-3" id="btn-eliminar-div">
                <div id="btn-eliminar"">
                <button v-if="index != 0" type="button" class="btn btn-primary" id="addHorario" @click="eliminarDia">Eliminar</button>
                </div>
            </div>
        </div>
        <button type="button" class="btn btn-primary" id="addHorario" @click="agregarDia">Agregar otro horario</button>
    </div>
    `
}

/* Variable contenedora de la instancia del componente horario */
var contenedorHorario = new Vue({
    el: '#componente_horario',
    components: {
        'horario': Horario
    }
})