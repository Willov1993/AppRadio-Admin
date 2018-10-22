const Segmento = {
    data() {
        return{
            emisoras: [],
            segmentos:[],
        }
    },
    methods: {
        agregarSegmento(){
            this.segmentos.push({'value': null, 'name':null})
        },
        eliminarSegmento(indice){
            this.segmentos.splice(indice, 1)
        },
        fillSegmentos(e,indice){
            this.segmentos[indice].nombre = e.target.value
        }
    },
    mounted(){
        this.agregarSegmento()
    },
    template:/*html*/`
    <div>
        <div v-for="(segmento, index) in segmentos" v-bind:key="index">
            <label for="emisoraSelect">Seleccione la Emisora</label>
            <select id="emisoraSelect" class="custom-select form-control" name="emisora" oninvalid="this.setCustomValidity('Ingrese una emisora válida')" required oninput="this.setCustomValidity('')" @change="fillSegmentos($event,index)">
                <option selected disabled>Seleccione la emisora</option>
                <option v-for="em in $parent.emisoras" :value="em.id">{{em.nombre}}</option>
            </select>
            <label for="segmentoSelect" id="lblSegmento">Seleccione el Segmento</label>
            <div class="form-row">
                <div class="form-group col-md-2">
                    <select id="segmentoSelect" v-bind:name="segmento" class="custom-select form-control">
                        <option disable selected value="">--</option>
                    </select>
                </div>
                <div v-if="index != 0" class="form-group col-md-2">
                    <button type="button" class="btn btn-primary" @click="eliminarSegmento(index)">Eliminar</button>
                </div>
                <div class="form-group col-md-2">
                    <button id="btn_agregar" v-if="index == segmentos.length - 1" type="button" class="btn btn-primary" @click="agregarSegmento">Agregar otro segmento</button>
                </div>
            </div>
        </div>
    </div>
    `
}

var contenedorSegmentos = new Vue({
    el: '#componente_segmento',
    components: {
        'segmento': Segmento
    },
    data: {
        emisoras: []
    },
    mounted: function () {
        var app= this;
        fetch('/api/emisoras')
        .then(function(response){
            return response.json();
        })
        .then(function(myJson){
            console.log(myJson);
            console.log("This prop:"+app.emisoras.length);
            for (var index in myJson){
               app.emisoras.push(myJson[index]);
            }
            console.log(app.emisoras);
        })
    }
})