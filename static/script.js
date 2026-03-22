async function loadNotes() {
    let res = await fetch("/get_notes");
    let data = await res.json();

    let list = document.getElementById("notesList");
    list.innerHTML = "";

    data.forEach(note => {
        let li = document.createElement("li");
        li.innerHTML = `${note[1]} 
        <button onclick="deleteNote(${note[0]})">X</button>`;
        list.appendChild(li);
    });
}

async function addNote() {
    let text = document.getElementById("noteInput").value;

    await fetch("/add_note", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({text})
    });

    loadNotes();
}

async function deleteNote(id) {
    await fetch(`/delete_note/${id}`, {
        method: "DELETE"
    });

    loadNotes();
}

loadNotes();
