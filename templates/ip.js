/* ** ** ** ** ** ** ** ** ** ** ** ** ** ** */
let ip = '{{ ip }}';
let aso = '{{ aso }}';
let asn = '{{ asn }}';
let iso_code = '{{ iso_code }}';
let continent_code = '{{ continent_code }}';
let country = '{{ country }}';
let continent = '{{ continent }}';
let zip_code = '{{ zip_code }}';
let state = '{{ state }}';
let state_code = '{{ state_code }}';
let city = '{{ city }}';
let latitude = '{{ latitude }}';
let longitude = '{{ longitude }}';
let author = '{{ author }}';
if (author != 'vsevolodhtml') {ip = 'Автор Всеволод html';console.log(ip);} else {console.log('IP и GEO полученно успешно!');}
/* ** ** ** ** ** ** ** ** ** ** ** ** ** ** */
let fulljson = `{\n  "ip": "` + ip + `",\n  "aso": "` + aso + `",\n  "asn": "` + asn + `",\n  "iso_code": "` + iso_code + `",\n  "continent_code": "` + continent_code + `",\n  "country": "` + country + `",\n  "continent": "` + continent + `",\n  "zip_code": "` + zip_code + `",\n  "state": "` + state + `",\n  "state_code": "` + state_code + `",\n  "city": "` + city + `",\n  "latitude": ` + latitude + `,\n  "longitude": ` + longitude + `,\n  "author": "vsevolodhtml"\n}`;
globalThis.geo = {
    go: function() {
        console.log(fulljson);
    },
    write: function(e) {
        document.body.append(fulljson);
    },
    print: function(e) {
        alert(fulljson);
    },
    help: function(e) {
        console.group('Инструкция:');console.log('geo.go(); -- обычный вывод GEO в консоль');console.log('geo.write(); -- добавить в документ JSON GEO');console.log('geo.print(); -- модальное окно с GEO');console.groupEnd();console.group('Пример:');console.log(fulljson);console.groupEnd();console.groupEnd();
    }
}
/* ** ** ** ** ** ** ** ** ** ** ** ** ** ** */