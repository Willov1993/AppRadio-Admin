function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

const Segmento = {
    data() {
        return{
            segmentosLocutor: [],
        }
    },
    methods: {
        agregarSegmento(){
            this.segmentosLocutor.push({'value': null, 'name':null})
        },
        eliminarSegmento(indice){
            this.segmentosLocutor.splice(indice, 1)
        },
        fillSegmentos(e,indice){
            var app = this;
            app.$parent.segmentos= []
            //this.segmentos[indice].nombre = e.target.value
            fetch('/api/' + e.target.value + '/segmentos',{
                method: "get",
                credentials: "same-origin",
                headers: {
                    "X-CSRFToken": getCookie("csrftoken"),
                    "Accept": "application/json",
                    "Content-Type": "application/json"  
                }
            })
            .then(function(response){
                return response.json();
            })
            .then(function(myJson){
                console.log("Json: " + myJson);
                for (var index in myJson){
                    app.$parent.segmentos.push(myJson[index]);
                }
                console.log("segmentos:" + JSON.stringify(app.$parent.segmentos));
            })
        }
    },
    mounted(){
        this.agregarSegmento()
    },
    template:/*html*/`
    <div>
        <div v-for="(segmento, index) in segmentosLocutor" v-bind:key="index">
            <label for="emisoraSelect">Seleccione la Emisora</label>
            <select id="emisoraSelect" class="custom-select form-control" name="emisora" oninvalid="this.setCustomValidity('Ingrese una emisora válida')" required oninput="this.setCustomValidity('')" @change="fillSegmentos($event,index)">
                <option selected disabled>Seleccione la emisora</option>
                <option v-for="em in $parent.emisoras" :value="em.id">{{em.nombre}}</option>
            </select>
            <label for="segmentoSelect" id="lblSegmento">Seleccione el Segmento</label>
            <div class="form-row">
                <div class="form-group col-md-2">
                    <select id="segmentoSelect" v-bind:name="segmento" class="custom-select form-control">
                        <option selected disabled>Seleccione el segmento</option>
                        <option v-for="seg in $parent.segmentos" :value="seg.id">{{seg.nombre}}</option>
                    </select>
                </div>
                <div v-if="index != 0" class="form-group col-md-2">
                    <button type="button" class="btn btn-primary" @click="eliminarSegmento(index)">Eliminar</button>
                </div>
                <div class="form-group col-md-2">
                    <button id="btn_agregar" v-if="index == segmentosLocutor.length - 1" type="button" class="btn btn-primary" @click="agregarSegmento">Agregar otro segmento</button>
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
        emisoras: [],
        segmentos: []
    },
    mounted: function () {
        var app= this;
        fetch('/api/emisoras',{
            method: "get",
            credentials: "same-origin",
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
                "Accept": "application/json",
                "Content-Type": "application/json"  
            }
        })
        .then(function(response){
            return response.json();
        })
        .then(function(myJson){
            for (var index in myJson){
               app.emisoras.push(myJson[index]);
            }
        })
    }
})