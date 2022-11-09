
async function main() {
    try {
        const res = await Promise.all(["1", "2"].map(url => download(url)))
        console.log("res " + res)
    } catch (error) {
        console.error(e)
    }
}

function download(url) {
    return new Promise((resolve, reject) => {
        try {
            console.log("Promise " + url)
            "Promise " + url
        } catch (e) {
            reject(e)
        }
    })
}

// Promise.all(["1", "2"].map(url => download(url)))
//     .then(res => console.log("res " + res))
//     .catch(e => console.error(e))
