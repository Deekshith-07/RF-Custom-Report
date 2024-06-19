
function showContent(section) {
    // Hide all sections
    var sections = document.getElementsByClassName('content');
    for (var i = 0; i < sections.length; i++) {
        sections[i].style.display = 'none';
    }

    // Show the selected section
    document.getElementById(section).style.display = 'block';

    // Remove the 'active' class from all sidebar links
    var sidebarLinks = document.querySelectorAll('.sidebar a');
    for (var i = 0; i < sidebarLinks.length; i++) {
        sidebarLinks[i].classList.remove('active');
    }

    // Add the 'active' class to the clicked sidebar link
    var activeLink = document.querySelector('.sidebar a[href="#' + section + '"]');
    if (activeLink) {
        activeLink.classList.add('active');
    }
}


function searchFunction(inputId, tableId) {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById(inputId);
    filter = input.value.toUpperCase();
    table = document.getElementById(tableId);
    tr = table.getElementsByTagName("tr");

    for (i = 1; i < tr.length; i++) {  // Start from 1 to skip the header row
        td = tr[i].getElementsByTagName("td")[1];  // Get the second column (index 1)
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}
