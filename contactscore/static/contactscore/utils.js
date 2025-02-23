
async function loadHomepageTotals() {
    // this is a demonstration of ajax - it could alternatively done using a template
    let req = await fetch("/api/totals");
    return await req.json();

}