#import required libraries
import fresh_tomatoes
import media

#The following lines of code creates the movie objects and their respective descriptions
shawshank_redemption = media.Movie("The Shawshank Redemption", 
	"Andy Dufresne (Tim Robbins) is sentenced to two consecutive life terms in prison for the murders of his wife and her lover and is sentenced to a tough prison. However, only Andy knows he didn't commit the crimes. While there, he forms a friendship with Red (Morgan Freeman), experiences brutality of prison life, adapts, helps the warden, etc., all in 19 years.",
	"https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
	"https://www.youtube.com/watch?v=6hB3S9bIaco")

inception = media.Movie("Inception",
	"A man in a suit with a gun in his right hand is flanked by five other individuals in the middle of a street which, behind them, is folded upwards.",
	"https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
	"https://www.youtube.com/watch?v=YoHD9XEInc0")

tenacious_d = media.Movie("Tenacious D In the Pick of Destiny",
	"Musicians JB (Jack Black) and KG (Kyle Gass) begin a friendship that could lead to the formation of the greatest rock band in the world. To make that dream come true, the righteous duo embark on a quest to find a legendary guitar pick that possesses supernatural powers.",
	"http://www.gstatic.com/tv/thumb/dvdboxart/159770/p159770_d_v7_aa.jpg",
	"https://www.youtube.com/watch?v=TXxQFMG86HA")

wolf_of_wall_street = media.Movie("The Wolf of Wall Street",
	"In 1987, Jordan Belfort (Leonardo DiCaprio) takes an entry-level job at a Wall Street brokerage firm. By the early 1990s, while still in his 20s, Belfort founds his own firm, Stratton Oakmont. Together with his trusted lieutenant (Jonah Hill) and a merry band of brokers, Belfort makes a huge fortune by defrauding wealthy investors out of millions. However, while Belfort and his cronies partake in a hedonistic brew of sex, drugs and thrills, the SEC and the FBI close in on his empire of excess.",
	"http://t1.gstatic.com/images?q=tbn:ANd9GcTm52BWbxXmwOpfz5rmx0BNBj79kSQoGpYPq4TVt07Jel5En6aC",
	"https://www.youtube.com/watch?v=iszwuX1AK6A")

enders_game = media.Movie("Ender's Game",
	"Young Ender Wiggin is recruited by the International Military to lead the fight against the Formics, a genocidal alien race which nearly annihilated the human race in a previous invasion.",
	"http://t1.gstatic.com/images?q=tbn:ANd9GcTaRaUQVkktc33gAipAmO38gV6z6BUN85qRxEjtj4nNJP2OfFcD",
	"https://www.youtube.com/watch?v=X5ev-nOWJH8")

pirates = media.Movie("Pirates of the Caribbean: The Curse of the Black Pearl",
	"Blacksmith Will Turner teams up with eccentric pirate Captain Jack Sparrow to save Turner's love, Elizabeth Swann, from undead pirates led by Jack's former mutinous first mate, Captain Barbossa. Jack wants revenge against Barbossa, who left him stranded on an island before stealing his ship, the Black Pearl, along with 882 pieces of cursed Aztec Gold.",
	"https://upload.wikimedia.org/wikipedia/en/0/0e/Pirates_of_the_Caribbean_movie.jpg",
	"https://www.youtube.com/watch?v=naQr0uTrH_s")

#lists the movies inside an array
movies = [shawshank_redemption, inception, tenacious_d, wolf_of_wall_street, enders_game, pirates]

#calls a function from the fresh_tomatoes file that opens a webpage that showcases the movies
fresh_tomatoes.open_movies_page (movies)
