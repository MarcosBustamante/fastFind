/**
 * Created by bustamante on 4/22/15.
 */
if(typeof jsutils === "undefined")
    jsutils = {};

jsutils.object_is_empty = function(object){
    for(key in object) return false;
    return true;
};
