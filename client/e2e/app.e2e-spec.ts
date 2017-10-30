import { ChattyClientPage } from './app.po';

describe('chatty-client App', () => {
  let page: ChattyClientPage;

  beforeEach(() => {
    page = new ChattyClientPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});
