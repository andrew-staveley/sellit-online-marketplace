import { useEffect, useState } from "react"
import ListingCard from "./ListingCard.js"

function HomePage() {
    const [listings, setListings] = useState([])

    useEffect(() => {
        fetch('/listings')
        .then((r) => r.json())
        .then((listingsArray) => {
            setListings(listingsArray);
        });
    }, []);

    return (
        <div>
            <h1>Welcome to Sellit Online Marketplace</h1>
            <ul>
                {listings.map((listing) => {
                    return<ListingCard key={listing.id} listing={listing}/>
                })}
            </ul>
        </div>
    )
}

export default HomePage;