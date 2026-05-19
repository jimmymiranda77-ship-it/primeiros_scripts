import * as readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";

const rl = readline.createInterface({ input, output });

try {
	const secret = 
		Math.floor(Math.random() * (20)) + 1;
	let tries = 0;
	let guess = 0;
	console.log("Estou pensando em um número entre 1 e 20");
	
	while (guess !== secret) {
		const text = await rl.question("Tente um chute: ");
		guess = parseInt(text,10);
		
		tries = tries + 1;
		
		if (guess <1 || guess > 20) {
			console.log("Essa tentiva está fora do intervalo. Tente novamente.");
		}  else if (guess < secret) {
			console.log("Muito baixo, tente novamente.");
		}  else if (guess > secret) {
			console.log("Muita alto, tente novamente");
		} else {
			console.log("Parabéns! Você conseguiu em", tries, "tentativas!");
		}
		}
	} finally {
		rl.close();
	}			
		
							
