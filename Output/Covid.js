const url = "Covid19_Data.json";

let states_list =[]
// // Get the data
d3.json(url).then(function(data) {
                    console.log(data)
                    


data.forEach (function(d){
                    if (states_list.includes(d.state)){console.log(`${d.state} already in list`);}
                    else {states_list.push(d.state);}
}

); 
console.log(states_list)
});

// Initiate the function
function init(){
// Use D3 to select the dropdown menu 
// Assign the value of the dropdown menu option to a variable
let dropdownMenu = d3.select("#selDataset");
d3.json(url).then((data) => {
                    console.log(data)

                    // Log the value of id for each iteration of the loop
states_list.forEach((id) => {
dropdownMenu.append("option").attr("value",id).text(id);
                 }); 
// First entry of the sample                 
let first_entry = states_list[0];
console.log(first_entry)
});
}

// Make the demographic info panel
function panel(selectedValue) {

    d3.json(url).then((data) => {

        // Create an array of the metadata objects
        let metadata = data.metadata;
        
        // Filter data where id = selected value
        let filteredData = metadata.filter((meta) => meta.id == selectedValue);
      
        // Assign the first object to obj variable
        let obj = filteredData[0]
        
        // Use .html("") to clear any existing metadata
        d3.select("#sample-metadata").html("");
  
        // Use Object.entries() to return key-value pairs
        // Reference: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries
        let results = Object.entries(obj);

        // Iterate through the entries array
        // Add a h5 child element for each key-value pair
        results.forEach(([key,value]) => {
            d3.select("#sample-metadata").append("h5").text(`${key}: ${value}`);
        });

        // Log the entries Array
        console.log(results);
    });
  }
  
init()

