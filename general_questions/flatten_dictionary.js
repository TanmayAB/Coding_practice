
function flatten_obj(original_obj, falttend_obj, gen_key) {

    for (let key in original_obj) {
        let new_key = '';
        if (typeof(original_obj[key]) === 'object') {
            if (gen_key === ''){
                new_key = key;
            } else {
                new_key = gen_key + '_' + key;
            }
            console.log("Calling recur with gen_key: " + gen_key);
            flatten_obj(original_obj[key], falttend_obj, new_key);
        } else {
            if (gen_key === ''){
                    new_key = key;
                } else {
                    new_key = gen_key + '_' + key;
                }
            console.log("Inserting: " +  gen_key + original_obj[key] );
            console.log(typeof(original_obj[key]));
            falttend_obj[new_key] = original_obj[key];
        }
    }

    return falttend_obj;
}

let obj = {
    a: { b: {c: 10}},
    d: [{e: 1}, {e: 2}],
    f: 'hello'
}

console.log(flatten_obj(obj, {}, ''));