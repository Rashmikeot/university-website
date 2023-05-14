console.log("working2");

// const schools_url =  "http://127.0.0.1:8000/api2/v1/department/";
const schools_url =  "http://127.0.0.1:8000/api2/v1/school/";




async function getSchoolsapi(url) {
  let response = await fetch(url);
  // Storing data in form of JSON
  const data = await response.json();
//   console.log(data);
    let schools_collection = "";
    let schools = document.getElementById(
    `schools`
    );
    
  data.map((school, index)=>{
    schools_collection += `<ul><li>School of ${school.name}</li><ul id="${school.name}">`;
    // console.log(school.School_id, school.name)
    const departments_url =  `http://127.0.0.1:8000/api2/v1/school/${school.School_id}/departments`;
    let departments_collection=''
    
    async function getDepartmentsapi(url, department_id) {
      let response = await fetch(url);
      let schools = document.getElementById(department_id);
      const department_data = await response.json();
      department_data.map((department, index)=>{
          // console.log("departments",department.Department_name)
          departments_collection += `<li>Department of ${department.Department_name}</li>`;
      })
      schools.innerHTML = departments_collection;
    }
    // getDepartmentsapi(departments_url)
    getDepartmentsapi(departments_url, school.name)
    schools_collection += `</ul></ul>`;
    console.log("ul",schools_collection);
    if (schools_collection !== undefined)
    schools.innerHTML =
    schools_collection;
  })
}

getSchoolsapi(schools_url);
