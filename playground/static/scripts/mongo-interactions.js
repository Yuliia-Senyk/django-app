async function addClick() {
        try {
            const response = await fetch('http://127.0.0.1:8000/playground/db', {
                method: 'POST',
            });
            if (response.ok) {
                console.log('good');
            } else {
                console.error('POST request failed');
            }
        } catch (error) {
            console.error('Error during POST request:', error);
        }
    }

async function updateClick() {
    try {
         const response = await fetch('http://127.0.0.1:8000/playground/db', {
               method: 'PUT',
           });
           if (response.ok) {
               console.log('good');
           } else {
            console.error('PUT request failed');
           }
    } 
    catch (error) {
        console.error('Error during PUT request:', error);
     }
}

async function deleteClick() {
    try {
        const response = await fetch('http://127.0.0.1:8000/playground/db', {
              method: 'DELETE',
          });
          if (response.ok) {
              console.log('good');
          } else {
           console.error('DELETE request failed');
          }
   } 
   catch (error) {
       console.error('Error during DELETE request:', error);
    }
}