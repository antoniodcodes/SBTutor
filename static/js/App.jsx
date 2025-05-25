import React, {useState, useEffect} from 'react'
import Flashcard from './components/Flashcard'

const App = () => {
  const [words, setWords] = useState([])
  const [filter, setFilter] =useState(0)
  
  const fetchWords = () => {
    cards = fetch('/words')
            .then(response => response.json())
            .then(data => setWords(data))
            .catch(error => console.log(error))
  }

  useEffect(() => {
    fetchWords();
  }, [words])
  
  // Filter by Difficulty Level
  const onChangeHandler = (evt) => {
    setFilter(parseInt(evt.target.value));
    if(filter !== 0){
    const filtered_words = words.filter(word => word.difficulty_level === filter);
    setWords(filtered_words);
    }
  }
  //TODO: Pass values into Flashcard component
  return (
    <>
      <select name='flashcard_filter' onChange={onChangeHandler} value={filter} className="">
        <option value="0">All</option>
        <option value="1">Level One</option>
        <option value="2">Level Two</option>
        <option value="3">Level Three</option>
      </select>
      {words && words.map(word => <Flashcard key={word.id} {...word}/>)}
    </>

  )
}