#!/usr/bin/node
const http = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
http.get(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const result = JSON.parse(body);
  result.characters.forEach(clink =>
    http.get(clink, function (error, response, body) {
      if (error) {
        console.error(error);
        return;
      }
      console.log(JSON.parse(body).name);
    })
  );
});
