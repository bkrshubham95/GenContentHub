import RadioButton from "./RadioButton"
import { useState } from "react"

export const Feedback = ({slogan , keywords}) => {
    const [creativity , setCreativity] = useState('medium')
    const [tone , setTone] = useState('medium')
    const [style , setStyle] = useState('medium')

    const sendPhraseFeedback = (e) => {
        fetch('http://127.0.0.1:5000/main/dump-feedback', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },

        body: JSON.stringify({ slogan :slogan,  modes : {creativity: creativity , style: style , tone : tone} , keywords: keywords}),
        })
        .then(response => alert("feedback saved!"))
        .catch(error => {
            alert("Feedback not saved")
        });
    }
    

    

    
    return <><div>
        <RadioButton mode={"creativity"} modeSetter = {setCreativity}/>
        <RadioButton mode={"style"} modeSetter = {setStyle}/>
        <RadioButton mode={"tone"} modeSetter = {setTone}/>
        <button type="submit" onClick={sendPhraseFeedback}>Send Phrase Feedback</button>
    </div>
    </>
}
