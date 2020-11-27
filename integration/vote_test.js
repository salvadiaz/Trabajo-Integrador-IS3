Feature('vote');

Scenario('I am on hme view', ({ I }) => {
    I.amOnPage('https://vote-is3.herokuapp.com')
    I.see('DOGS')
    I.see('CATS')
    I.see('Processed by container ID')
    I.seeElement('//*[@id="content-container-center"]/h3')
    I.seeElement('//*[@id="a"]')
    I.seeElement('//*[@id="b"]')
});


Scenario('Testing Result View', ({ I }) => {
    I.amOnPage('https://result-is3.herokuapp.com/');
    I.see('CATS');
    I.see('DOGS');
    I.seeElement('//*[@id="background-stats-2"]');
    I.seeElement('//*[@id="background-stats-1"]');
});