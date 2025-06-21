import React from 'react'

const Flashcard = (props) => {

  return (
    <div className="card" style="width: 18rem;">
      <img src={props.image_url} className="card-img-top"  />
      <div className="card-body">
        <h5 className="card-title">{props.name}</h5>
        <p className="card-text">
          <strong>Pronunciation: </strong>
          {props.pronunciation} <br />
          <strong>Definition: </strong>
          {props.definition} <br />
          <strong>Parts Of Speech: </strong>
          {props.parts_of_speech}
          <br />
          <strong>Etymology: </strong>
          {props.etymology}
          <br />
          <strong>Level: </strong>
          {props.difficulty_level}
          <br />
          <strong>Examples: </strong>
          {props.usage}
        </p>
        <a href={props.audio_url} className="card-link">
          <i className="bi bi-play-circle"></i>
        </a>
      </div>
    </div>
  );
}