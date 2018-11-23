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
                'tipo': null, 
                'dia_semana': null,
                'hora_inicio': null,
                'hora_fin': null
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
                <label>Frecuencia</label>
                <select v-model="horario.tipo" name="tipo" id="tipoInput" class="custom-select form-control" required>
                    <option value="Diaria">Diaria</option>
                    <option value="Semanal">Semanal</option>
                    <option value="Mensual">Mensual</option>
                    <option value="Anual">Anual</option>
                </select>
            </div>

            <div class="form-group col-md-2">
                <label>Dia</label>
                <select v-model="horario.dia_semana" name="dia_semana" id="diaInput" class="custom-select form-control" required>
                    <option value="Lunes">Lunes</option>
                    <option value="Martes">Martes</option>
                    <option value="Miércoles">Miércoles</option>
                    <option value="Jueves">Jueves</option>
                    <option value="Viernes">Viernes</option>
                    <option value="Sabado">Sábado</option>
                    <option value="Domingo">Domingo</option>
                </select>
            </div>
            <div class="form-group col-md-2">
                <label>Hora de inicio</label>
                <input v-model="horario.hora_inicio" name="hora_inicio" type="time" class="form-control" required>
            </div>
            <div class="form-group col-md-2">
                <label>Hora fin</label>
                <input v-model="horario.hora_fin" name = "hora_fin" type="time" class="form-control" required>
            </div>
            <div class="form-group col-md-2" id="btn-eliminar-div">
                <div id="btn-eliminar"">
                <button v-if="index != 0" type="button" class="btn btn-primary" id="addHorario" @click="eliminarDia">Eliminar</button>
                </div>
            </div>
        </div>
        <button type="button" class="btn btn-primary" id="addHorario" @click="agregarDia">Agregar otra frecuencia</button>
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

